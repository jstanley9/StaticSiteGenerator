import unittest
from textnode import TextNode, TextType

from splitnodesdelimiter import split_nodes_delimiter


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_simple_text(self):
        text = 'simple string'
        node0 = TextNode(text, TextType.TEXT)
        nodes = [node0]
        delimiter = '**'
        new_nodes = split_nodes_delimiter(nodes, delimiter, TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        expected = f'{node0}'
        self.assertEqual(f'{new_nodes[0]}', expected)

    def test_simple_bold(self):
        text = 'simple **bold** text'
        node0 = TextNode(text, TextType.TEXT)
        nodes = [node0]
        delimiter = '**'
        new_nodes = split_nodes_delimiter(nodes, delimiter, TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        expected0 = f'{TextNode('simple ', TextType.TEXT)}'
        self.assertEqual(f'{new_nodes[0]}', expected0)
        expected1 = f'{TextNode('bold', TextType.BOLD)}'
        self.assertEqual(f'{new_nodes[1]}', expected1)
        expected2 = f'{TextNode(' text', TextType.TEXT)}'
        self.assertEqual(f'{new_nodes[2]}', expected2)
    
    def test_begin_bold(self):
        text = '**bold** message'
        node0 = TextNode(text, TextType.TEXT)
        nodes = [node0]
        delimiter = '**'
        new_nodes = split_nodes_delimiter(nodes, delimiter, TextType.BOLD)
        self.assertEqual(len(new_nodes), 2)
        expected0 = f'{TextNode('bold', TextType.BOLD)}'
        self.assertEqual(f'{new_nodes[0]}', expected0)
        expected1 = f'{TextNode(' message', TextType.TEXT)}'
        self.assertEqual(f'{new_nodes[1]}', expected1)

    def test_end_bold(self):
        text = 'bold **ending**'
        node0 = TextNode(text, TextType.TEXT)
        nodes = [node0]
        delimiter = '**'
        new_nodes = split_nodes_delimiter(nodes, delimiter, TextType.BOLD)
        self.assertEqual(len(new_nodes), 2)
        expected0 = f'{TextNode('bold ', TextType.TEXT)}'
        self.assertEqual(f'{new_nodes[0]}', expected0)
        expected1 = f'{TextNode('ending', TextType.BOLD)}'
        self.assertEqual(f'{new_nodes[1]}', expected1)

    def test_only_bold(self):
        text = '**everything is bold**'
        node0 = TextNode(text, TextType.TEXT)
        nodes = [node0]
        delimiter = '**'
        new_nodes = split_nodes_delimiter(nodes, delimiter, TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        expected0 = f'{TextNode('everything is bold', TextType.BOLD)}'
        self.assertEqual(f'{new_nodes[0]}', expected0)

    def test_simple_italic(self):
        text = 'simple *italic* text'
        node0 = TextNode(text, TextType.TEXT)
        nodes = [node0]
        delimiter = '*'
        new_nodes = split_nodes_delimiter(nodes, delimiter, TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        expected0 = f'{TextNode('simple ', TextType.TEXT)}'
        self.assertEqual(f'{new_nodes[0]}', expected0)
        expected1 = f'{TextNode('italic', TextType.ITALIC)}'
        self.assertEqual(f'{new_nodes[1]}', expected1)
        expected2 = f'{TextNode(' text', TextType.TEXT)}'
        self.assertEqual(f'{new_nodes[2]}', expected2)

    def test_simple_code(self):
        text = 'simple `x = x + y` code block'
        node0 = TextNode(text, TextType.TEXT)
        nodes = [node0]
        delimiter = '`'
        new_nodes = split_nodes_delimiter(nodes, delimiter, TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        expected0 = f'{TextNode('simple ', TextType.TEXT)}'
        self.assertEqual(f'{new_nodes[0]}', expected0)
        expected1 = f'{TextNode('x = x + y', TextType.CODE)}'
        self.assertEqual(f'{new_nodes[1]}', expected1)
        expected2 = f'{TextNode(' code block', TextType.TEXT)}'
        self.assertEqual(f'{new_nodes[2]}', expected2)
