import os
import re
import shutil
from typing import NoReturn

from textblock import markdown_to_html_node


def clear_dir(path: str):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)


def mirror(source: str, destination: str, *, verbose=False):
    clear_dir(destination)

    for entry in os.scandir(source):
        src_path = entry.path
        dst_path = src_path.replace(source, destination)

        if entry.is_dir():
            mirror(src_path, dst_path, verbose=verbose)
            continue

        if verbose:
            print(f"{src_path} -> {dst_path}")
            shutil.copy2(src_path, dst_path)


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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.scandir(dir_path_content):
        src_path = entry.path
        dst_path = src_path.replace(dir_path_content, dest_dir_path)

        if entry.is_dir():
            generate_pages_recursive(src_path, template_path, dst_path)
            continue

        if not src_path.endswith(".md"):
            continue

        dst_path = dst_path.removesuffix(".md") + ".html"
        generate_page(src_path, template_path, dst_path)
