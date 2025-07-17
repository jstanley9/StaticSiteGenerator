import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_no_url_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertEqual(node, node2)

    def test_unequal_text(self):        
        node = TextNode("Some other text", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

    def test_unequal_type(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

    def test_unequal_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "")
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertEqual(node, node2)

    def test_unequal_actual_urls(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://something.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://something.com")
        self.assertEqual(node, node2)




if __name__ == "__main__":
    unittest.main()