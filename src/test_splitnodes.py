import unittest
from textnode import TextNode, TextType

from splitnodes import split_nodes_delimiter, split_nodes_link, split_nodes_image, text_to_textnodes


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

    def test_bold_bold(self):
        text = '**bold** middle **ending**'
        node0 = TextNode(text, TextType.TEXT)
        nodes = [node0]
        delimiter = '**'
        new_nodes = split_nodes_delimiter(nodes, delimiter, TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        expected0 = f'{TextNode('bold', TextType.BOLD)}'
        self.assertEqual(f'{new_nodes[0]}', expected0)
        expected1 = f'{TextNode(' middle ', TextType.TEXT)}'
        self.assertEqual(f'{new_nodes[1]}', expected1)
        expected2 = f'{TextNode('ending', TextType.BOLD)}'
        self.assertEqual(f'{new_nodes[2]}', expected2)


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

    def test_split_nodes_image(self):
        init_text = 'This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)'
        node =TextNode(init_text, TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes[0], TextNode('This is text with an ', TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode('image', TextType.IMAGES, 'https://i.imgur.com/zjjcJKZ.png'))
        self.assertEqual(new_nodes[2], TextNode(' and another ', TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode('second image', TextType.IMAGES, 'https://i.imgur.com/3elNhQu.png'))
        self.assertEqual(len(new_nodes), 4, 'Image nodes not properly split out')

    def test_split_nodes_link(self):
        init_text = 'This is text with a link [to boot dev](https://www.boot.dev ) and [to youtube](https://www.youtube.com/@bootdotdev)'
        node = TextNode(init_text, TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0], TextNode('This is text with a link ', TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode('to boot dev', TextType.LINKS, 'https://www.boot.dev'))
        self.assertEqual(new_nodes[2], TextNode(' and ', TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode('to youtube', TextType.LINKS, 'https://i.imgur.com/3elNhQu.png'))
        self.assertEqual(len(new_nodes), 4, 'Link nodes not properly split')

    def test_split_mixed_images_and_links(self):
        init_text = 'This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) then a link [to youtube](https://www.youtube.com/@bootdotdev)'
        node = TextNode(init_text, TextType.TEXT)
        new_nodes = split_nodes_image([node])
        new_nodes = split_nodes_link(new_nodes)
        self.assertEqual(new_nodes[0], TextNode('This is text with an ', TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode('image', TextType.IMAGES, 'https://i.imgur.com/zjjcJKZ.png'))
        self.assertEqual(new_nodes[2], TextNode(' then a link ', TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode('to youtube', TextType.LINKS, 'https://i.imgur.com/3elNhQu.png'))
        self.assertEqual(len(new_nodes), 4, 'Link nodes not properly split')

    def test_text_to_textnodes(self):
        text = 'This is **text** with an _italic_ word and a `code block` and an ' + \
               '![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes[0], TextNode('This is ', TextType.TEXT))
        self.assertEqual(nodes[1], TextNode('text', TextType.BOLD))
        self.assertEqual(nodes[2], TextNode(' with an ', TextType.TEXT))
        self.assertEqual(nodes[3], TextNode('italic', TextType.ITALIC))
        self.assertEqual(nodes[4], TextNode(' word and a ', TextType.TEXT))
        self.assertEqual(nodes[5], TextNode('code block', TextType.CODE))
        self.assertEqual(nodes[6], TextNode(' and an ', TextType.TEXT))
        self.assertEqual(nodes[7], TextNode('obi wan image', TextType.IMAGES))
        self.assertEqual(nodes[8], TextNode(' and a ', TextType.TEXT))
        self.assertEqual(nodes[9], TextNode('link', TextType.LINKS))
        self.assertEqual(len(nodes), 10, 'Expected 10 nodes')

    def test_text_to_textnodes_text_only(self):
        text = 'This is a simple text string'

        nodes = text_to_textnodes(text)
        self.assertEqual(nodes[0], TextNode('This is a simple text string', TextType.TEXT))
        self.assertEqual(len(nodes), 1, 'Expected 1 node')
