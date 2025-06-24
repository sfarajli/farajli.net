import yaml

def parse_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != '---':
        return {}

    frontmatter_lines = []
    for line in lines[1:]:
        if line.strip() == '---':
            break
        frontmatter_lines.append(line)

    frontmatter_str = ''.join(frontmatter_lines)
    frontmatter = yaml.safe_load(frontmatter_str) or {}

    return frontmatter
