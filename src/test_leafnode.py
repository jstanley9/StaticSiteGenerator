import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_just_text(self):
        text = "Just some plain old text"
        node = LeafNode(None, text)
        self.assertEqual(node.to_html(), text)

    def test_None_value(self):
        with self.assertRaises(ValueError) as context:
            text = None
            node = LeafNode(text)
            html_text = node.to_html()

        self.assertEqual(str(context.exception), 'A "value" is required for a leaf node')

    def test_all_stuff(self):
        href = {'href': 'https://somewhat.invalid.www.com'}
        text = 'yeah, this link is invalid'
        tag = 'a'
        node = LeafNode(tag = tag, value = text, props = href)
        result = node.to_html()
        self.assertEqual(result, '<a href="https://somewhat.invalid.www.com">yeah, this link is invalid</a>')

    def test_a_paragraph(self):
        text = 'Purple People Eater'
        tag = 'p'
        node = LeafNode(tag, text)
        result = node.to_html()
        match_html = f'<{tag}>{text}</{tag}>'
        self.assertEqual(result, match_html)