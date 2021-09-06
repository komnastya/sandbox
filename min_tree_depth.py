# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
        self.left = left
        self.right = right


def min_tree_depth(node: Node) -> int:
    if node is None:
        return 0
    left = min_tree_depth(node.left)
    right = min_tree_depth(node.right)
    if left == 0 and right == 0:
        return 1
    if left == 0 and right != 0:
        return 1 + right
    if left != 0 and right == 0:
        return 1 + left
    return 1 + min(left, right)
