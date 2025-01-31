import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_conversion(self):
        test_cases = [
            (
                TextNode("normal text node", TextType.TEXT),
                "normal text node",
                "TEXT Node",
            ),
            (
                TextNode("bold text node", TextType.BOLD),
                "<b>bold text node</b>",
                "BOLD Node",
            ),
            (
                TextNode("italic text node", TextType.ITALIC),
                "<i>italic text node</i>",
                "ITALIC Node",
            ),
            (
                TextNode("#!/usr/bin/env code text node", TextType.CODE),
                "<code>#!/usr/bin/env code text node</code>",
                "CODE Node",
            ),
            (
                TextNode("link text node", TextType.LINK, "https://example.com"),
                '<a href="https://example.com">link text node</a>',
                "LINK Node",
            ),
            (
                TextNode(
                    "image text node", TextType.IMAGE, "https://example.com/example.png"
                ),
                '<img src="https://example.com/example.png" alt="image text node"></img>',
                "IMAGE Node",
            ),
        ]

        for given, expected, case_id in test_cases:
            self.assertEqual(
                text_node_to_html_node(given).to_html(),
                expected,
                msg=f"{case_id} test failed",
            )


if __name__ == "__main__":
    unittest.main()
