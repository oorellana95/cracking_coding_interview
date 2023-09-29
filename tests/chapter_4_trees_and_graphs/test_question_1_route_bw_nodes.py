import pytest

from questions.chapter_4_trees_and_graphs.graph import Node
from questions.chapter_4_trees_and_graphs.question_1_route_bw_nodes import has_route_bfs, has_route_dfs


@pytest.fixture
def sample_graph():
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')

    A.children.extend([B, C])
    B.children.extend([D, E])
    C.children.extend([F])

    return A, B, C, D, E, F


def test_has_route_dfs_positive(sample_graph):
    A, B, C, D, E, F = sample_graph

    assert has_route_dfs(A, B) == True
    assert has_route_dfs(A, D) == True
    assert has_route_dfs(A, E) == True
    assert has_route_dfs(B, E) == True
    assert has_route_dfs(B, D) == True
    assert has_route_dfs(C, F) == True
    assert has_route_dfs(A, F) == True


def test_has_route_dfs_negative(sample_graph):
    A, B, C, D, E, F = sample_graph

    assert has_route_dfs(B, F) == False
    assert has_route_dfs(F, A) == False
    assert has_route_dfs(C, D) == False


def test_has_route_bfs_positive(sample_graph):
    A, B, C, D, E, F = sample_graph

    assert has_route_bfs(A, B) == True
    assert has_route_bfs(A, D) == True
    assert has_route_bfs(A, E) == True
    assert has_route_bfs(B, E) == True
    assert has_route_bfs(B, D) == True
    assert has_route_bfs(C, F) == True
    assert has_route_bfs(A, F) == True


def test_has_route_bfs_negative(sample_graph):
    A, B, C, D, E, F = sample_graph

    assert has_route_bfs(B, F) == False
    assert has_route_bfs(F, A) == False
    assert has_route_bfs(C, D) == False

