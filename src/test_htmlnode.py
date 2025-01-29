import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_repr(self):
        self.assertEqual(
            repr(HTMLNode()),
            "HTMLNode(tag=None, value=None, props={})",
        )

    def test_no_tohtml(self):
        with self.assertRaises(NotImplementedError):
            HTMLNode().to_html()

    def test_props_to_html(self):
        self.assertEqual(
            HTMLNode(
                "script", props={"defer": "", "src": "out-4.5.44.js"}
            ).props_to_html(),
            ' defer="" src="out-4.5.44.js"',
        )


if __name__ == "__main__":
    unittest.main()
