from depth_of_n_ary_tree import Node, maxDepth


def test_max_depth():
    assert maxDepth(None) == 0
    assert maxDepth(Node()) == 1
    assert maxDepth(Node(val=None, children=[Node()])) == 2
    assert maxDepth(Node(val=None, children=[Node(val=None, children=[Node()])])) == 3
    assert (
        maxDepth(
            Node(
                val=None,
                children=[Node(val=None, children=[Node(val=None, children=[Node()])])],
            )
        )
        == 4
    )
    assert (
        maxDepth(
            Node(
                val=None,
                children=[
                    Node(
                        val=None,
                        children=[
                            Node(val=None, children=[Node(val=None, children=[Node()])])
                        ],
                    )
                ],
            )
        )
        == 5
    )
    assert (
        maxDepth(
            Node(
                val=None,
                children=[
                    Node(
                        val=None,
                        children=[
                            Node(
                                val=None,
                                children=[
                                    Node(
                                        val=None,
                                        children=[Node(val=None, children=[Node()])],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            )
        )
        == 6
    )
