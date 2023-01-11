import sys

from edge import Edge
from collections import deque


class Graph:
    """This class is graph's adjacency list representation"""

    def __init__(self, max_vertex_idx):
        if max_vertex_idx < 0:
            raise ValueError("Vertex index can't be negative!")
        self.graph = []
        self.max_vertices = max_vertex_idx
        self.create_vertices()

    def create_vertices(self):
        i = 0
        while i <= self.max_vertices:
            self.graph.append(None)
            i += 1

    def add_edge(self, e: Edge):
        if (e.v1 > self.max_vertices) or (e.v2 > self.max_vertices) :
            raise ValueError('Vertex index is out of range')

        if self.graph[e.v1] is None:
            self.graph[e.v1] = []

        if not self.is_in_graph(e):
            self.graph[e.v1].append(e.v2)

    def remove_edge(self, e: Edge):
        if not self.is_in_graph(e):
            raise ValueError("Given Edge doesn't exists")
        self.graph[e.v1].remove(e.v2)

    def is_in_graph(self, e: Edge):
        if self.graph[e.v1] is None:
            return False
        return e.v2 in self.graph[e.v1]

    def print(self):
        print('Graph:')
        idx = 0
        for e in self.graph:
            if e is not None:
                print('Vertex: {}->{}'.format(idx, [val for val in e]))
            else:
                print('Vertex: {}->{}'.format(idx, e))
            idx += 1
        print()

    def sort_lists(self):
        for sub_list in self.graph:
            if not sub_list is None:
                sub_list.sort()

    @staticmethod
    def load_from_file(file: str):
        try:
            with open(file, 'r') as fs:
                n = int(fs.readline())
                g = Graph(n)
                [g.add_edge(Edge(int(line.split(',')[0].strip()), int(line.split(',')[1].strip()))) for line in
                 fs.readlines()]
            return g
        except FileNotFoundError:
            print('No such file')
            sys.exit()


def print_bfs(instance: Graph, start: int):
    instance.sort_lists()
    to_visit = deque()
    visited = set()
    visited.add(start)
    to_visit.append(start)

    while to_visit:
        current = to_visit.popleft()
        neighbours = instance.graph[current]
        print(current, end=' ')
        for vertex in neighbours:
            if not vertex in visited:
                visited.add(vertex)
                to_visit.append(vertex)
    print()


def print_dfs(instance: Graph, start: int):
    visited = set()
    instance.sort_lists()

    def dfs(idx: int, v: set):
        v.add(idx)
        print(idx, end=' ')
        neighbours = instance.graph[idx]
        for vertex in neighbours:
            if not vertex in visited:
                dfs(vertex, v)

    dfs(start, visited)
    print()
