import pytest
from min_tree_depth import min_tree_depth, Node


def test_min_tree_depth():
    assert min_tree_depth(None) == 0
    assert min_tree_depth(Node()) == 1
    assert min_tree_depth(Node(left=None, right=None)) == 1 # the same as min_tree_depth(Node())
    assert min_tree_depth(Node(left=None, right=Node())) == 1
    assert min_tree_depth(Node(left=Node(), right=Node())) == 2
    assert min_tree_depth(Node(left=None, right=Node(left=None, right=Node()))) == 1
    assert min_tree_depth(Node(left=Node(left=None, right=Node()), right=Node(left=None, right=Node()))) == 2
