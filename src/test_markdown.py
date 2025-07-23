import unittest

from markdown import markdown_to_blocks


class TestMarkDown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_empty(self):

        md = ''
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_none(self):
        md = None
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
