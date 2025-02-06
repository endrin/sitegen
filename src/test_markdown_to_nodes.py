import unittest

from htmlnode import LeafNode, ParentNode
from textblock import markdown_to_html_node


class TestHTMLNode(unittest.TestCase):
    maxDiff = None

    def test_markdown_to_html_h_p_ul(self):
        markdown = """
# HEADER

Paragraph

- List item
- List item

[link](somewhere)

![image](somewhere)

*italics*

**bold**
"""
        nodes = ParentNode(
            "div",
            [
                ParentNode("h1", [LeafNode(None, "HEADER")]),
                ParentNode("p", [LeafNode(None, "Paragraph")]),
                ParentNode(
                    "ul",
                    [
                        ParentNode("li", [LeafNode(None, "List item")]),
                        ParentNode("li", [LeafNode(None, "List item")]),
                    ],
                ),
                ParentNode("p", [LeafNode("a", "link", {"href": "somewhere"})]),
                ParentNode(
                    "p",
                    [LeafNode("img", "", props={"src": "somewhere", "alt": "image"})],
                ),
                ParentNode("p", [LeafNode("i", "italics")]),
                ParentNode("p", [LeafNode("b", "bold")]),
            ],
        )

        self.assertEqual(markdown_to_html_node(markdown), nodes)

    def test_markdown_to_html_h3_bq_ol_code(self):
        markdown = """
### HEADER3

> Multi
> line
> quote

1. List item
2. List item

```
[link](somewhere)
![image](somewhere)
```
"""
        nodes = ParentNode(
            "div",
            [
                ParentNode("h3", [LeafNode(None, "HEADER3")]),
                ParentNode("blockquote", [LeafNode(None, "Multi\nline\nquote")]),
                ParentNode(
                    "ol",
                    [
                        ParentNode("li", [LeafNode(None, "List item")]),
                        ParentNode("li", [LeafNode(None, "List item")]),
                    ],
                ),
                ParentNode(
                    "pre",
                    [
                        LeafNode(
                            "code",
                            "[link](somewhere)\n![image](somewhere)",
                        )
                    ],
                ),
            ],
        )

        self.assertEqual(markdown_to_html_node(markdown), nodes)


if __name__ == "__main__":
    unittest.main()
