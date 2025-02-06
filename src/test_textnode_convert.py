import unittest

from textnode import TextNode, TextType
from transforms import text_node_to_html_node, text_to_textnodes


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


class TestTextToTextNodes(unittest.TestCase):
    def test_all_splits(self):
        input = (
            "This is **text** "
            "with an *italic* word "
            "and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )
        expected_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        actual_output = text_to_textnodes(input)

        # self.maxDiff = None
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
