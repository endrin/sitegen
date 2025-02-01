from enum import Enum
from typing import Optional, Self

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: Self):
        return (
            self.text == other.text
            and self.text_type is other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise NotImplementedError("This type of text node is not here yet")


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
