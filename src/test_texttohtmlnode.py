import unittest
from texttohtmlnode import text_node_to_html_node, extract_title

from textnode import TextNode, TextType

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        text = 'some text'
        node = text_node_to_html_node(TextNode(text, TextType.TEXT))
        html = node.to_html()
        expect = text
        self.assertEqual(html, text)

    def test_bold(self):
        text = 'This is boldtext!'
        node = text_node_to_html_node(TextNode(text, TextType.BOLD))
        html = node.to_html()
        expect = f'<b>{text}</b>'
        self.assertEqual(html, expect)

    def test_italic(self):
        text = 'This is italicized text!'
        node = text_node_to_html_node(TextNode(text, TextType.ITALIC))
        html = node.to_html()
        expect = f'<i>{text}</i>'
        self.assertEqual(html, expect)

    def test_code(self):
        text = 'quip += "you betcha!"'
        node = text_node_to_html_node(TextNode(text, TextType.CODE))
        html = node.to_html()
        expect = f'<code>{text}</code>'
        self.assertEqual(html, expect)
        
    def test_links(self):
        text = 'pet adoption'
        node = text_node_to_html_node(TextNode(text, TextType.LINKS, 'https://petadoption.org'))
        html = node.to_html()
        expect = f'<a href="https://petadoption.org">{text}</a>'
        self.assertEqual(html, expect)

    def test_images(self):
        text = 'silly cat'
        node = text_node_to_html_node(TextNode(text, TextType.IMAGES, 'c:/pictures/sillycat.png'))
        html = node.to_html()
        expect = f'<img src="c:/pictures/sillycat.png" alt="{text}"></img>'
        self.assertEqual(html, expect)

    def test_pull_h1_content_index_md(self):
        markdown = './content/index.md'
        result = extract_title(markdown)
        expected = 'Tolkien Fan Club'
        self.assertEqual(result, expected)

    def test_pull_h1_content_readme_md(self):
        markdown = './README.md'
        result = extract_title(markdown)
        expected = 'StaticSiteGenerator'
        self.assertEqual(result, expected)

    def test_extract_title_no_title(self):
        with self.assertRaises(Exception) as context:
            markdown = './template.html'
            title = extract_title(markdown)

        self.assertEqual(str(context.exception), f'Markdown file: {markdown} is missing heading ("# " => <h1>)')
