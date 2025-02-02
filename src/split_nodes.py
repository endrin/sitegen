import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    def split_node(node: TextNode):
        [left, middle, right] = node.text.split(delimiter, maxsplit=3)
        base_type = node.text_type if not node.url else TextType.TEXT
        return [
            TextNode(left, base_type),
            TextNode(middle, text_type),
            TextNode(right, base_type),
        ]

    return list(*(split_node(n) for n in old_nodes))


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    image_re = re.compile(r"!\[([^\]]+)\]\(([^\)]+)\)")
    return image_re.findall(text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    link_re = re.compile(r"(?<!!)\[([^\]]+)\]\(([^\)]+)\)")
    return link_re.findall(text)
