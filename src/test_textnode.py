import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_w_url(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://example.com")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://example.com")
        self.assertEqual(node, node2)

    def test_ne_text(self):
        node = TextNode("This is a text node 1", TextType.CODE, "https://")
        node2 = TextNode("This is a text node 2", TextType.CODE, "https://")
        self.assertNotEqual(node, node2)

    def test_ne_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://")
        self.assertNotEqual(node, node2)

    def test_ne_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://#1")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://#2")
        self.assertNotEqual(node, node2)

    def test_ne_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("texnode test", TextType.IMAGE, "https://www.boot.dev")
        self.assertEqual(
            repr(node), "TextNode(texnode test, image, https://www.boot.dev)"
        )


if __name__ == "__main__":
    unittest.main()
