from typing import List, Optional


class Node:
    def __init__(self, val: int = None, children: List = None):
        self.val = val  # type: Optional[int]
        self.children = children  # type: Optional[List[Node]]


# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Definition for a Node.
def maxDepth(node: Optional[Node]) -> int:
    if node is None:
        return 0
    if not node.children:
        return 1
    return 1 + max((maxDepth(child) for child in node.children))
