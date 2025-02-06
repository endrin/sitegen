import unittest

from textblock import block_to_block_type


class TestBlockTypes(unittest.TestCase):
    def test_pragraph(self):
        block = "Just a plain text with no extra formatting"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_heading(self):
        blocks = [
            "# Heading level 1",
            "## Heading level 2",
            "### Heading level 3",
            "#### Heading level 4",
            "##### Heading level 5",
            "###### Heading level 6",
        ]

        for block in blocks:
            self.assertEqual(block_to_block_type(block), "heading", msg=block)

        not_heading = "####### Heading level 7"
        self.assertEqual(block_to_block_type(not_heading), "paragraph")

    def test_code(self):
        block = """```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```"""
        self.assertEqual(block_to_block_type(block), "code")

    def test_quote(self):
        blocks = {
            "simgle line": "> Dorothy followed her through many of the beautiful rooms in her castle.",
            "multi line": """> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.""",
            "nested": """> Dorothy followed her through many of the beautiful rooms in her castle.
>
> > The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.""",
        }
        for description, block in blocks.items():
            self.assertEqual(block_to_block_type(block), "quote", msg=description)

    def test_unordered_list(self):
        blocks = {
            "-": """- First item
- Second item
- Third item
- Fourth item """,
            "*": """* First item
* Second item
* Third item
* Fourth item """,
        }
        for description, block in blocks.items():
            self.assertEqual(
                block_to_block_type(block), "unordered_list", msg=description
            )

    def test_ordered_list(self):
        block = """1. First item
2. Second item
3. Third item
4. Fourth item"""
        self.assertEqual(block_to_block_type(block), "ordered_list")
