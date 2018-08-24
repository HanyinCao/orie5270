import unittest
import tree.print_tree as tp


class TestTree(unittest.TestCase):

    def test_tree_1(self):
        t = tp.Tree(tp.Node(1, None, None))
        assert t.print_tree() == [['1']]

    def test_tree_2(self):
        node_1 = tp.Node(2, None, None)
        node_2 = tp.Node(3, None, None)
        node_root = tp.Node(1, node_1, node_2)
        t = tp.Tree(node_root)
        assert t.print_tree() == [['|', '1', '|'],
                                  ['2', '|', '3']]

    def test_tree_3(self):
        node_root = tp.Node(1, None, None)
        node_root.left = tp.Node(2, None, None)
        node_root.left.left = tp.Node(3, None, None)
        t = tp.Tree(node_root)
        assert t.print_tree() == [['|', '|', '|', '1', '|', '|', '|'],
                                  ['|', '2', '|', '|', '|', '|', '|'],
                                  ['3', '|', '|', '|', '|', '|', '|']]

    def test_tree_4(self):
        d_2 = tp.Node(7, None, None)
        c_1 = tp.Node(5, None, d_2)
        b_1 = tp.Node(3, c_1, None)
        b_2 = tp.Node(4, None, None)
        node_root = tp.Node(2, b_1, b_2)
        t = tp.Tree(node_root)
        assert t.print_tree() == [['|', '|', '|', '|', '|', '|', '|', '2',
                                   '|', '|', '|', '|', '|', '|', '|'],
                                  ['|', '|', '|', '3', '|', '|', '|',
                                   '|', '|', '|', '|', '4', '|', '|', '|'],
                                  ['|', '5', '|', '|', '|', '|', '|', '|',
                                   '|', '|', '|', '|', '|', '|', '|'],
                                  ['|', '|', '7', '|', '|', '|', '|',
                                   '|', '|', '|', '|', '|', '|', '|', '|']]
