import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        node1 = HTMLNode("bla1", "bla2", "bla3", {
        "href": "https://www.google.com",
        "target": "_blank",
        })
        print(node1, node1.props_to_html())

    def test2(self):
        node1 = HTMLNode()
        print(node1)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node.props_to_html())
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

        




if __name__ == "__main__":
    unittest.main()