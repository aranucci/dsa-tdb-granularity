import os
import json
import re
import frontmatter
from pathlib import Path

def parse_document_metadata(content, metadata):
    """
    Tries to extract 'Effective Date' or 'Last Updated' from the text 
    if it's not already in the YAML frontmatter.
    """
    # Look for dates like 'August 2025' or 'January 1, 2025'
    date_pattern = r"(Effective|Last updated|Date of Last Revision|Updated|Last modified|Last revised|Dated|January|February|March|April|May|June|July|August|September|October|November|December):\s*([A-Za-z]+ \d{1,2}, \d{4}|[A-Za-z]+ \d{4})"
    match = re.search(date_pattern, content, re.IGNORECASE)
    
    extracted_date = match.group(2) if match else "No effective date found."
    
    return {
        "platform_name": metadata.get("service", "Unknown Platform"),
        "contract_type": metadata.get("title", "Terms and Conditions Contract"),
        "effective_date": metadata.get("date", extracted_date),
        "region": metadata.get("region", "EU/EEA"),
        "source_url": metadata.get("url", "No URL provided.")
    }

def convert_to_dsa_json(input_root, output_root):
    input_path = Path(input_root)
    
    for md_file in input_path.rglob('*.md'):
        if md_file.name.startswith('.') or 'README' in md_file.name or 'LICENSE' in md_file.name:
            continue

        with open(md_file, 'r', encoding='utf-8') as f:
            try:
                post = frontmatter.load(f)
                
                # Setup Paths
                relative_path = md_file.relative_to(input_path)
                output_folder = Path(output_root) / relative_path.parent
                output_folder.mkdir(parents=True, exist_ok=True)

                # 1. Build Document Info
                doc_info = parse_document_metadata(post.content, post.metadata)

                # 2. Build Content Tree (Splitting by Headers)
                content_tree = []

                # Matches '# Header', '## Header', or '1. Header' style
                sections = re.split(r'\n(?=#|##|###|\*\*|(?:\d+\\\.?\s))', post.content)
                
                for idx, section in enumerate(sections):
                    lines = section.strip().split('\n')
                    if not lines: continue
                    
                    header = lines[0].replace('#', '').strip()
                    body = "\n".join(lines[1:]).strip()
                    
                    if body:
                        content_tree.append({
                            "section_id": str(idx + 1),
                            "header": header,
                            "text_content": body,
                            "dsa_mapping_suggestions": [] # Placeholder for Step 3
                        })

                # 3. Final JSON Structure
                final_data = {
                    "document_info": doc_info,
                    "content_tree": content_tree,
                    "global_metadata": {
                        "source_file": str(relative_path),
                        "processor_version": "1.1"
                    }
                }

                # Save JSON
                json_filename = md_file.stem + ".json"
                with open(output_folder / json_filename, 'w', encoding='utf-8') as out:
                    json.dump(final_data, out, indent=4, ensure_ascii=False)

            except Exception as e:
                print(f"Error processing {md_file}: {e}")

    print(f"Structured JSONs are in: {output_root}")

# Execution
convert_to_dsa_json('./vlop-vlose-versions', './converted_jsons')