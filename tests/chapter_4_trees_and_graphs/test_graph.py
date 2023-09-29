from questions.chapter_4_trees_and_graphs.graph import Node, depth_first_search


def test_depth_first_search_and_visit():
    a, b, c, d, e = Node("A"), Node("B"), Node("C"), Node("D"), Node("E")

    a.children = [b, c]
    b.children = [d, e]

    import io
    from contextlib import redirect_stdout

    with io.StringIO() as output:
        with redirect_stdout(output):
            depth_first_search(a)
        printed_output = output.getvalue()

    # Check if the printed output matches the expected visit order
    expected_output = "A\nB\nD\nE\nC\n"
    assert printed_output == expected_output

    # Check if all nodes in the tree have been visited
    assert a.visited
    assert b.visited
    assert c.visited
    assert d.visited
    assert e.visited
