import pytest

from questions.chapter_4_trees_and_graphs.graph import Node, depth_first_search, breadth_first_search


@pytest.fixture
def sample_graph():
    a, b, c, d, e = Node("A"), Node("B"), Node("C"), Node("D"), Node("E")

    a.children = [b, c]
    b.children = [d, e]

    return a


@pytest.mark.parametrize("search_func, expected_output", [
    (depth_first_search, "A\nB\nD\nE\nC\n"),
    (breadth_first_search, "A\nC\nB\nE\nD\n"),
])
def test_search_and_visit(sample_graph, search_func, expected_output):
    import io
    from contextlib import redirect_stdout

    with io.StringIO() as output:
        with redirect_stdout(output):
            search_func(sample_graph)
        printed_output = output.getvalue()

    assert printed_output == expected_output

