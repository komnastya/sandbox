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
        self.left = left
        self.right = right


# Count quantity


def node_count(node: Node) -> int:
    if node is None:
        return 0
    else:
        return 1 + node_count(node.left) + node_count(node.right)


# Count height


def max_tree_depth(node: Node) -> int:
    if node is None:
        return 0
    return 1 + max(max_tree_depth(node.left), max_tree_depth(node.right))
