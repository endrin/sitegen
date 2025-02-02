import unittest

from split_nodes import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
)
from textnode import TextNode, TextType


class TestSplitNodes(unittest.TestCase):
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


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        text = (
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) "
            "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        images = extract_markdown_images(text)
        expected_images = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]

        self.assertEqual(images, expected_images)

    def test_extract_links(self):
        text = (
            "This is text with a link [to boot dev](https://www.boot.dev) "
            "and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        links = extract_markdown_links(text)
        expected_links = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(links, expected_links)

    def test_extract_links_and_images_together(self):
        text = (
            "This is text with a link [to boot dev](https://www.boot.dev)"
            "but actually it is ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        )
        images = extract_markdown_images(text)
        links = extract_markdown_links(text)

        expected_images = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        expected_links = [("to boot dev", "https://www.boot.dev")]

        self.assertEqual(images, expected_images)
        self.assertEqual(links, expected_links)
