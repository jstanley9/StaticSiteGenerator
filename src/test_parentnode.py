import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_imbedded_url_ref(self):
        para_start = LeafNode(None, "Let's jump out to another urls @ ")
        para_end = LeafNode(None, ". That's it.")
        italics = LeafNode("i", "an obtuse web site")
        embolden = ParentNode("b", [italics])
        url = ParentNode("a", [embolden], {"href": "https://www.someobtusewebsite.ill"})
        paragraph = ParentNode("p", [para_start, url, para_end])
        actual_html = paragraph.to_html()
        expected_html = '<p>Let\'s jump out to another urls @ <a href="https://www.someobtusewebsite.ill"><b><i>an obtuse web site</i></b></a>. That\'s it.</p>'
        self.assertEqual(actual_html,  expected_html)
                         
def main():
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())#, "<div><span>child</span></div>")

if __name__  == '__main__':
    main()   
