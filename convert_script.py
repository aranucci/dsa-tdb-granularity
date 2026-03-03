import os
import json
import frontmatter
from pathlib import Path

def md_to_individual_jsons(input_dir, output_parent_dir):
    # 1. Create the output folder if it doesn't exist
    if not os.path.exists(output_parent_dir):
        os.makedirs(output_parent_dir)
        print(f"Created directory: {output_parent_dir}")

    # 2. Iterate through all .md files in the repository
    count = 0
    for path in Path(input_dir).rglob('*.md'):
        with open(path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            metadata = post.metadata
            content = post.content
            
            # Simple header parsing
            sections = []
            current_section = {"header": "Introduction", "text": ""}
            for line in content.split('\n'):
                if line.startswith('#'):
                    if current_section["text"].strip():
                        sections.append(current_section)
                    header_text = line.replace('#', '').strip()
                    current_section = {"header": header_text, "text": ""}
                else:
                    current_section["text"] += line + "\n"
            
            if current_section["text"].strip():
                sections.append(current_section)

            # Create the structured data
            service_name = metadata.get("service", path.parent.name).lower().replace(" ", "_")
            # file_date = str(metadata.get("date", "unknown_date"))
            
            service_data = {
                "service": service_name,
                # "date": file_date,
                "url": metadata.get("url", ""),
                "sections": sections
            }
            
            # 3. Save as an individual JSON file
            # Example filename: tiktok_2023-08-25.json
            json_filename = f"{service_name}.json"
            output_path = os.path.join(output_parent_dir, json_filename)
            
            with open(output_path, 'w', encoding='utf-8') as out:
                json.dump(service_data, out, indent=4, ensure_ascii=False)
            
            count += 1

    print(f"Finished! Processed {count} files into the '{output_parent_dir}' folder.")

# Run the script
repo_path = './vlop-vlose-versions' 
output_path = './structured_t_and_c'
md_to_individual_jsons(repo_path, output_path)