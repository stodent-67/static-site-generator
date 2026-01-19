import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        node1 = HTMLNode("bla1", "bla2", "bla3", {
        "href": "https://www.google.com",
        "target": "_blank",
        })
        print(node1, node1.props_to_html())
        




if __name__ == "__main__":
    unittest.main()