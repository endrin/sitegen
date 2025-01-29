import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_w_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_to_html_value_required(self):
        with self.assertRaises(ValueError):
            _ = LeafNode(tag="p", props={"display": "none"}).to_html()

    def test_empty_repr(self):
        self.assertEqual(
            repr(LeafNode("a", "Click me!", {"href": "https://www.google.com"})),
            "LeafNode(tag='a', value='Click me!', children=None, props={'href': 'https://www.google.com'})",
        )


if __name__ == "__main__":
    unittest.main()
