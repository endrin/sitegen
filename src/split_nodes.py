import re

from textnode import TextNode, TextType

_IMAGE_RE_ = re.compile(r"!\[([^\]]+)\]\(([^\)]+)\)")
_LINK_RE_ = re.compile(r"(?<!!)\[([^\]]+)\]\(([^\)]+)\)")


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
    return _IMAGE_RE_.findall(text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return _LINK_RE_.findall(text)


def split_by_pattern(text, pattern):
    indices = [0, *(pos for m in pattern.finditer(text) for pos in m.span()), None]
    return [text[i:j] for i, j in zip(indices, indices[1:])]


def split_nodes_image(old_nodes):
    def do_split(node):
        for chunk in split_by_pattern(node.text, _IMAGE_RE_):
            if m := _IMAGE_RE_.fullmatch(chunk):
                alt_text, url = m.group(1, 2)
                yield TextNode(alt_text, TextType.IMAGE, url)
            else:
                yield TextNode(chunk, TextType.TEXT)

    return [
        new_node
        for old_node in old_nodes
        for new_node in do_split(old_node)
        if new_node.text != ""
    ]


def split_nodes_link(old_nodes):
    def do_split(node):
        for chunk in split_by_pattern(node.text, _LINK_RE_):
            if m := _LINK_RE_.fullmatch(chunk):
                alt_text, url = m.group(1, 2)
                yield TextNode(alt_text, TextType.LINK, url)
            else:
                yield TextNode(chunk, TextType.TEXT)

    return [
        new_node
        for old_node in old_nodes
        for new_node in do_split(old_node)
        if new_node.text != ""
    ]
