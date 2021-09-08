from typing import Optional


# Find tree height
#                        Node
#       left              |               right
#         ----------------+------------------
#         |                                 |
#    x----+-----                       -----+-----
#              |                       |         |
#          x---+---x                ---+---x x---+---x
#                                   |
#                               x---+---x


class Node:
    def __init__(self, left=None, right=None):
        self.left = left  # type: Optional[Node]
        self.right = right  # type: Optional[Node]


# Counts the number of nodes in the given tree root.
def node_count(node: Optional[Node]) -> int:
    if node is None:
        return 0
    else:
        return 1 + node_count(node.left) + node_count(node.right)


# Count height from the given tree root.
def max_tree_depth(node: Optional[Node]) -> int:
    if node is None:
        return 0
    return 1 + max(max_tree_depth(node.left), max_tree_depth(node.right))
