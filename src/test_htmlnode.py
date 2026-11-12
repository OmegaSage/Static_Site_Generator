import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_ene(self):
        node = HTMLNode('', '', [], props={"href": "https://www.google.com", "target": "_blank"})
        node2 = ' href="https://www.google.com" target="_blank"'
        print(repr(node2))
        self.assertEqual(node.props_to_html(), node2)

    def test_two(self):
        node = HTMLNode('','',[],{})
        node2 = ''
        print(repr(node2))
        self.assertEqual(node.props_to_html(), node2)

    def test_three(self):
        node = HTMLNode("abc", "123", ["123","abc"], {"cat":"meow"})
        node2 = ' cat="meow"'
        print(repr(node2))
        self.assertEqual(node.props_to_html(), node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_q(self):
        node1 = LeafNode("a", "26", {"aaaa": "bbbb"})
        node2 = '<a aaaa="bbbb">26</a>'
        self.assertEqual(node1.to_html(), node2)

    def test_leaf_to_html_r(self):
        node = LeafNode(None, None, None)
        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()
