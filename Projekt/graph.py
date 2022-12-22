from edge import Edge
from collections import deque


class Graph:
    """This class is graph's adjacency list representation"""

    def __init__(self, max_vertex_idx):
        self.graph = []
        self.max_vertices = max_vertex_idx + 1
        self.create_vertices()

    def create_vertices(self):
        i = 0
        while i < self.max_vertices:
            self.graph.append(None)
            i += 1

    def add_edge(self, e: Edge):
        if self.graph[e.v1] is None:
            self.graph[e.v1] = []

        if not self.is_in_graph(e):
            self.graph[e.v1].append(e.v2)

    def remove_edge(self, e: Edge):
        if not self.is_in_graph(e):
            raise ValueError('Given Edge doesn\'t exists')
        self.graph[e.v1].remove(e.v2)

    def is_in_graph(self, e: Edge):
        return e.v2 in self.graph[e.v1]

    def print(self):
        print('Graph:')
        idx = 0
        for e in self.graph:
            if e is not None:
                print('Vertex: {}->{}'.format(idx, [val for val in e]))
            idx += 1
        print()

    def from_file(self, file):
        pass

    def sort_lists(self):
        for sub_list in self.graph:
            sub_list.sort()


def print_bfs(instance: Graph, start: int):
    instance.sort_lists()
    to_visit = deque()
    visited = set()
    visited.add(start)
    to_visit.append(start)

    while to_visit:
        current = to_visit.popleft()
        neighbours = instance.graph[current]
        print(current)
        for vertex in neighbours:
            if not vertex in visited:
                visited.add(vertex)
                to_visit.append(vertex)


def print_dfs(instance: Graph, start: int):
    visited = set()
    instance.sort_lists()
    def dfs(idx: int, v: set):
        v.add(idx)
        print(idx)
        neighbours = instance.graph[idx]
        for vertex in neighbours:
            if not vertex in visited:
                dfs(vertex, v)
    dfs(start, visited)


if __name__ == '__main__':
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

    print_dfs(gph, 1)
