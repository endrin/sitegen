import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


class TestTextNodeSplit(unittest.TestCase):
    def test_split_to_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_link(self):
        node = TextNode(
            "This is a link with **a very important** title",
            TextType.LINK,
            "https://example.com",
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_nodes = [
            TextNode("This is a link with ", TextType.TEXT),
            TextNode("a very important", TextType.BOLD),
            TextNode(" title", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected_nodes)
