import unittest

from blocktype import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_simple_string(self):
        block = 'Simple paragraph.'
        result = block_to_block_type(block)
        expected = BlockType.PARAGRAPH
        self.assertEqual(result, expected)

    def test_heading_1(self):
        block = '# Heading 1'
        result = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(result, expected)

    def test_heading_6(self):
        block = '###### Heading 6'
        result = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(result, expected)

    def test_heading_2(self):
        block = '## Heading 2'
        result = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(result, expected)

    def test_heading_3(self):
        block = '### Heading 3'
        result = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(result, expected)
 
    def test_heading_4(self):
        block = '#### Heading 4'
        result = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(result, expected)
 
    def test_heading_5(self):
        block = '##### Heading 5'
        result = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(result, expected)

    def test_heading_7(self):
        block = '####### Heading 7'
        result = block_to_block_type(block)
        expected = BlockType.PARAGRAPH
        self.assertEqual(result, expected)

    def test_heading_nospace(self):
        block = '##Heading No Space'
        result = block_to_block_type(block)
        expected = BlockType.PARAGRAPH
        self.assertEqual(result, expected)

    def test_code_block(self):
        text = '''```
        block = '##Heading No Space'
        result = block_to_block_type(block)
        expected = BlockType.PARAGRAPH
        self.assertEqual(result, expected)
        ```'''
        expected = BlockType.CODE
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_code_block_justopening(self):
        text = '''```'''
        expected = BlockType.PARAGRAPH
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_code_block_empty(self):
        text = '''``````'''
        expected = BlockType.CODE
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_quote_block(self):
        text = '>single line'
        expected = BlockType.QUOTE
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_quote_multiline(self):
        text = '>first line\n>second line\n>third line'
        expected = BlockType.QUOTE
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_quote_multiline_not(self):
        text = '>first line\n second line\n>third line'
        expected = BlockType.PARAGRAPH
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_unordered_block(self):
        text = '- single line\n- second line'
        expected = BlockType.UNORDERED_LIST
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_unordered_multiline(self):
        text = '- first line\n- second line\n- third line'
        expected = BlockType.UNORDERED_LIST
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_unordered_multiline_not(self):
        text = '>first line\n-second line\n>third line'
        expected = BlockType.PARAGRAPH
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_ordered_block(self):
        text = '1. single line\n2.second line'
        expected = BlockType.PARAGRAPH
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_ordered_multiline(self):
        text = '1. first line\n2. second line\n3. third line'
        expected = BlockType.ORDERED_LIST
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_ordered_multiline_not(self):
        text = '1. first line\n2. second line\n4. third line'
        expected = BlockType.PARAGRAPH
        result = block_to_block_type(text)
        self.assertEqual(result, expected)
