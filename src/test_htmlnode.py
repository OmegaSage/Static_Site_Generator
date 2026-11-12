import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
#Testing base node: HTMLNode
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

#Testing LeafNode
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

#Test ParentNode
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


    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
            )



if __name__ == "__main__":
    unittest.main()
