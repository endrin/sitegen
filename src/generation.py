import os
import re
from typing import NoReturn

from textblock import markdown_to_html_node


def extract_title(markdown: str) -> str | NoReturn:
    if m := re.match(r"^#\s+(.*)", markdown.lstrip()):
        return m.group(1)

    raise ValueError("page has no title")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as md_f:
        markdown = md_f.read()

    with open(template_path) as tmpl_f:
        template = tmpl_f.read()

    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()

    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as html_f:
        html_f.write(html)
