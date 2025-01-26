from enum import Enum
from typing import Optional, Self


class TextType(Enum):
    NORMAL = "normal"
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
