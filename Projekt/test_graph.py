import pytest
import graph as g
from edge import Edge


def test_init():
    with pytest.raises(ValueError):
        gph = g.Graph(-1)

    gph = g.Graph(2)
    assert gph.max_vertices == 2
    for el in gph.graph:
        assert el is None


def test_add_edge():
    gph = g.Graph(2)

    with pytest.raises(ValueError):
        gph.add_edge(Edge(4, 5))

    gph.add_edge(Edge(0, 1))
    assert 1 in gph.graph[0]

    gph.add_edge(Edge(0, 0))
    assert 0 in gph.graph[0]


def test_remove_edge():
    gph = g.Graph(2)

    with pytest.raises(ValueError):
        gph.remove_edge(Edge(0, 0))

    gph.add_edge(Edge(0, 1))
    assert 1 in gph.graph[0]

    gph.remove_edge(Edge(0, 1))
    assert not 1 in gph.graph[0]


def test_is_in_graph():
    gph = g.Graph(2)
    assert not gph.is_in_graph(Edge(0, 0))

    gph.add_edge(Edge(0, 1))
    assert gph.is_in_graph(Edge(0, 1))


def test_sort_lists():
    gph = g.Graph(4)
    gph.add_edge(Edge(0, 4))
    gph.add_edge(Edge(0, 3))
    gph.add_edge(Edge(0, 2))
    gph.add_edge(Edge(0, 1))

    gph.add_edge(Edge(4, 1))
    gph.add_edge(Edge(4, 2))
    gph.add_edge(Edge(4, 3))
    gph.sort_lists()

    assert gph.graph[0] == [1, 2, 3, 4]
    assert gph.graph[4] == [1, 2, 3]
    assert gph.graph[1] is None
    assert gph.graph[2] is None
    assert gph.graph[3] is None


if __name__ == '__main__':
    pytest.main()
