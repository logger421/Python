import os
import sys

from edge import Edge
from collections import deque


class Graph:
    """This class is graph's adjacency list representation"""

    def __init__(self, max_vertex_idx:int, directed:bool=True):
        if max_vertex_idx < 0:
            raise ValueError("Vertex index can't be negative!")
        self.directed = directed
        self.graph = []
        self.max_vertices = max_vertex_idx
        self.create_vertices()

    def create_vertices(self):
        i = 0
        while i <= self.max_vertices:
            self.graph.append(None)
            i += 1

    def add_edge(self, e: Edge):
        if (e.v1 > self.max_vertices) or (e.v2 > self.max_vertices):
            raise ValueError('Vertex index is out of range')

        if self.graph[e.v1] is None:
            self.graph[e.v1] = []

        if not self.is_in_graph(e):
            self.graph[e.v1].append(e.v2)

        if not self.directed:
            if self.graph[e.v2] is None:
                self.graph[e.v2] = []

            if not self.is_in_graph(e):
                self.graph[e.v2].append(e.v1)

    def remove_edge(self, e: Edge):
        if not self.is_in_graph(e):
            raise ValueError("Given Edge doesn't exists")
        self.graph[e.v1].remove(e.v2)
        if not self.directed:
            self.graph[e.v2].remove(e.v1)

    def is_in_graph(self, e: Edge):
        if self.graph[e.v1] is None:
            return False
        if not self.directed:
            return e.v2 in self.graph[e.v1] and e.v1 in self.graph[e.v2]
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
                is_directed = eval(fs.readline())
                g = Graph(n, is_directed)
                [g.add_edge(Edge(int(line.split(' ')[0].strip()), int(line.split(' ')[1].strip()))) for line in
                 fs.readlines()]
            return g
        except FileNotFoundError:
            print('No such file')
            sys.exit()

    @staticmethod
    def save_to_file(g, file: str):
        with open(file, 'w') as fs:
            fs.write('{}\n'.format(g.max_vertices))
            fs.write('{}\n'.format(g.directed))
            idx = 0
            for e in g.graph:
                if e is not None:
                    [fs.write('{} {}\n'.format(idx, val)) for val in e]
                idx += 1
            fs.flush()
            os.fsync(fs.fileno())


def print_bfs(instance: Graph, start: int, log: bool = False):
    """Use log parameter if you want to return BFS list representation"""
    instance.sort_lists()
    to_visit = deque()
    visited = set()
    visited.add(start)
    to_visit.append(start)
    result = list()
    while to_visit:
        current = to_visit.popleft()
        result.append(current)
        neighbours = instance.graph[current]
        if not log: print(current, end=' ')
        for vertex in neighbours:
            if not vertex in visited:
                visited.add(vertex)
                to_visit.append(vertex)
    if log:
        return result


def print_dfs(instance: Graph, start: int, log: bool = False):
    """Use log parameter if you want to return DFS list representation"""
    visited = set()
    instance.sort_lists()
    result = list()

    def dfs(idx: int, v: set, res: list):
        v.add(idx)
        if not log: print(idx, end=' ')
        res.append(idx)
        neighbours = instance.graph[idx]
        for vertex in neighbours:
            if not vertex in visited:
                dfs(vertex, v, res)

    dfs(start, visited, result)
    if log:
        return result
