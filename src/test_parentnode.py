import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_no_children(self):
        node = ParentNode("p", [])

        self.assertEqual(
            node.to_html(),
            "<p></p>",
        )

    def test_to_html_tag_required(self):
        with self.assertRaises(ValueError):
            _ = ParentNode(None, []).to_html()


if __name__ == "__main__":
    unittest.main()
