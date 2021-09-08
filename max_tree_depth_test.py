from max_tree_depth import Node, max_tree_depth


def test_max_tree_depth():
    assert max_tree_depth(None) == 0
    assert max_tree_depth(Node()) == 1
    assert max_tree_depth(Node(left=Node(), right=Node())) == 2
    assert max_tree_depth(Node(left=None, right=Node(left=None, right=Node()))) == 3
