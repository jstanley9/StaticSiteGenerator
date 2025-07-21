import unittest

from extractimagesandlinks import extract_markdown_images, extract_markdown_links

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_simple_string(self):
        text = 'Simple string'
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])

    def test_single_images(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)'
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_two_images(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_two_links(self):
        text = 'This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)'
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_image_and_link(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)'
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]
        self.assertEqual(extract_markdown_images(text), expected)
        expected2 = [('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(extract_markdown_links(text), expected2)

    def test_link_and_image(self):
        text = 'This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://www.youtube.com/@bootdotdev)'
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]
        self.assertEqual(extract_markdown_links(text), expected)
        expected2 = [('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(extract_markdown_images(text), expected2)

    def test_unclosed_1st_images(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        expected = [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_unclosed_2nd_images(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg'
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]
        self.assertEqual(extract_markdown_images(text), expected)        