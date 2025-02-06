import unittest

from textblock import markdown_to_blocks


class TestSplitNodes(unittest.TestCase):
    def test_simple_split(self):
        input = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        blocks = markdown_to_blocks(input)

        self.assertEqual(blocks, expected_blocks)

    def test_split_with_too_much_empty_lines(self):
        input = """
# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.






* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        blocks = markdown_to_blocks(input)

        self.assertEqual(blocks, expected_blocks)

    def test_split_but_ensure_no_enclosing_blanks(self):
        input = """




# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item






"""
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        blocks = markdown_to_blocks(input)

        self.assertEqual(blocks, expected_blocks)
