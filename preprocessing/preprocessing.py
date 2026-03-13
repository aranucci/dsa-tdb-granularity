import os
import re
from pathlib import Path
from markdown_it import MarkdownIt
import frontmatter

md = MarkdownIt()

def read_markdown_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def remove_html_comments(content: str) -> str:
    """Remove any HTML comments."""
    return re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

def normalize_headings(content: str) -> str:
    """Normalize heading levels and spacing."""
    lines = content.split('\n')
    result = []
    for line in lines:
        if re.match(r'^#+\s', line):
            # Write single space after heading markers
            line = re.sub(r'^(#+)\s+', r'\1 ', line)
        result.append(line)
    return '\n'.join(result)

def remove_extra_whitespace(content: str) -> str:
    """Remove blank lines and whitespace."""
    lines = content.split('\n')
    lines = [line.rstrip() for line in lines]
    result = []
    prev_blank = False
    for line in lines:
        if line.strip():
            result.append(line)
            prev_blank = False
        elif not prev_blank:
            result.append(line)
            prev_blank = True
    return '\n'.join(result)

def clean_markdown(content: str) -> str:
    tokens = md.parse(content)
    cleaned_tokens = []
    current_header = None

    for token in tokens:
        if token.type in ['heading_open', 'heading_close']:
            if token.type == 'heading_open':
                current_header = token.markup + ' '  # e.g., '# ', '## '
            else:
                current_header = None
        elif token.type == 'paragraph_open':
            cleaned_tokens.append(current_header or '')
        elif token.type == 'inline':
            content = token.content.strip()
            # remove URLs
            if content:
                token.content = re.sub(r'http\S+', '', content)
            cleaned_tokens.append(token.content)

    return '\n'.join(cleaned_tokens)

def preprocess_markdown(file_path: str) -> str:
    content = read_markdown_file(file_path)
    content = remove_html_comments(content)
    content = normalize_headings(content)
    content = remove_extra_whitespace(content)
    content = clean_markdown(content)
    return content


def process_directory(input_directory: str, output_directory: str = None) -> None:
    input_path = Path(input_directory)
    for md_file in input_path.rglob('*.md'):
        if md_file.name.startswith('.') or 'README' in md_file.name or 'LICENSE' in md_file.name:
            continue

        with open(md_file, 'r', encoding='utf-8') as f:
            try: 
                post = frontmatter.load(f)

                relative_path = md_file.relative_to(input_path)
                output_folder = Path(output_directory) / relative_path.parent
                output_folder.mkdir(parents=True, exist_ok=True)

                processed_content = preprocess_markdown(md_file)
                output_path = output_folder / md_file.name
                with open(output_path, 'w', encoding='utf-8') as out:
                    out.write(processed_content)

            except Exception as e:
                print(f"Error processing {md_file}: {e}")

process_directory('./vlop-vlose-versions', './processed_data')