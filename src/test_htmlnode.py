import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_null_HTMLNode(self):
        node = HTMLNode()
        self.assertEqual(f'{node}', '')

    def test_tag_HTMLSNode(self):
        node = HTMLNode(tag = 'PoundSand')
        self.assertEqual(f'{node}', '"tag": "PoundSand"')

    def test_value_HTMLSNode(self):
        node = HTMLNode(value = 'Public Domain')
        self.assertEqual(f'{node}', '"value": "Public Domain"')

    def test_children_HTMLSNode(self):
        children = ['tickle', 'me', 'Elmo']
        node = HTMLNode(children = children)
        self.assertListEqual(node.children, children)

    def test_props_HTMLSNode(self):
        props = {'path': 'https://chukles.laugh', 'style': ['bold', 'italic']}
        node = HTMLNode(props = props)
        self.assertDictEqual(node.props, props)  

    def test_all_HTMLSNode(self):
        children = ['tickle', 'me', 'Elmo']
        props = {'path': 'https://chukles.laugh', 'style': ['bold', 'italic']}
        node = HTMLNode('PoundSand', 'Public Domain', children, props)
        self.assertEqual(node.tag, 'PoundSand')
        self.assertEqual(node.value, 'Public Domain')
        self.assertListEqual(node.children, children)
        self.assertDictEqual(node.props, props)

    def test_props(self):
        props = {'path': 'https://chukles.laugh', 'style': ['bold', 'italic']}
        node = HTMLNode('PoundSand', 'Public Domain', props = props)
        self.assertEqual(node.props_to_html(), ' path="https://chukles.laugh" style="[\'bold\', \'italic\']"')