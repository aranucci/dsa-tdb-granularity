import os
import json
import frontmatter
from pathlib import Path

def md_to_structured_json(directory_path, output_file):
    all_terms = []

    # Iterate through all .md files in the repository
    # vlop-vlose-versions usually contains subdirectories for each service
    for path in Path(directory_path).rglob('*.md'):
        with open(path, 'r', encoding='utf-8') as f:
            # Parse YAML metadata (frontmatter) and content
            post = frontmatter.load(f)
            
            # Extract metadata (service name, date, etc.)
            metadata = post.metadata
            content = post.content
            
            # Simple structure: split content by headers to make it "mappable"
            sections = []
            lines = content.split('\n')
            current_section = {"header": "Introduction", "text": ""}
            
            for line in lines:
                if line.startswith('#'):
                    # Save previous section if it has content
                    if current_section["text"].strip():
                        sections.append(current_section)
                    
                    # Start new section
                    header_level = line.count('#')
                    header_text = line.replace('#', '').strip()
                    current_section = {"header": header_text, "level": header_level, "text": ""}
                else:
                    current_section["text"] += line + "\n"
            
            # Add last section
            if current_section["text"].strip():
                sections.append(current_section)

            # Combine metadata and structured content
            service_data = {
                "file_name": path.name,
                "service": metadata.get("service", path.parent.name),
                "date": str(metadata.get("date", "")),
                "url": metadata.get("url", ""),
                "content_sections": sections
            }
            
            all_terms.append(service_data)

    # Save to JSON
    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump(all_terms, out, indent=4, ensure_ascii=False)
    
    print(f"Successfully processed {len(all_terms)} documents into {output_file}")

# Usage
# Point this to your local clone of the repository
repo_path = './vlop-vlose-versions' 
md_to_structured_json(repo_path, 'dsa_terms_structured.json')