import unittest

from generation import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_just_title(self):
        input = "# A Title"
        expected = "A Title"
        self.assertEqual(extract_title(input), expected)

    def test_title_with_extra(self):
        input = "# A Title\n\nA Paragraph"
        expected = "A Title"
        self.assertEqual(extract_title(input), expected)

    def test_title_with_whitespace(self):
        input = "\n             \n\n# A Title\n\nA Paragraph"
        expected = "A Title"
        self.assertEqual(extract_title(input), expected)

    def test_title_not_at_start(self):
        input = (
            "## A wrongly formatted title\n             \n\n# A Title\n\nA Paragraph"
        )
        with self.assertRaises(ValueError):
            _ = extract_title(input)


if __name__ == "__main__":
    unittest.main()
