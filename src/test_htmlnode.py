import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_ene(self):
        node = HTMLNode('', '', [], props={"href": "https://www.google.com", "target": "_blank"})
        print(repr(node.props_to_html()))
        node2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), node2)

    def test_two(self):
        node = HTMLNode('','',[],{})
        node2 = ''
        self.assertEqual(node.props_to_html(), node2)

    def test_three(self):
        node = HTMLNode("abc", "123", ["123","abc"], {"cat":"meow"})
        print(repr(node.props_to_html()))
        print(node.props_to_html())
        node2 = ' cat="meow"'
        self.assertEqual(node.props_to_html(), node2)

if __name__ == "__main__":
    unittest.main()
