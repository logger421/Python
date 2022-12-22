from graph import Graph
from edge import Edge

if __name__ == '__main__':
    # bfs example:
    gph = Graph(7)
    gph.add_edge(Edge(1, 0))
    gph.add_edge(Edge(1, 2))
    gph.add_edge(Edge(1, 4))

    gph.add_edge(Edge(0, 1))
    gph.add_edge(Edge(0, 5))
    gph.add_edge(Edge(5, 0))

    gph.add_edge(Edge(2, 1))
    gph.add_edge(Edge(2, 6))

    gph.add_edge(Edge(4, 1))
    gph.add_edge(Edge(4, 6))
    gph.add_edge(Edge(4, 3))

    gph.add_edge(Edge(3, 4))

    gph.add_edge(Edge(6, 4))
    gph.add_edge(Edge(6, 2))

    gph.add_edge(Edge(7, 7))
    gph.print()

    print_bfs(gph, 1)