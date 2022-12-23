import graph as g
from edge import Edge


def create_test_graph():
    gph = g.Graph(7)
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
    return gph


def view():
    print('-' * 44)
    print("Select one of options or type 'q' to exit: ")
    print('-' * 44)
    print('1) Create graph')
    print('2) Bfs example')
    print('3) Dfs example')
    print('-' * 44)


def read_edges(gph: g.Graph):
    print("Insert your graph's edges or type 'q' to quit")
    print('Enter pair of integers (space separated):')
    vertices = None
    while True:
        vertices = input('> ')
        if vertices == 'q': break
        vertices = tuple([int(edge) for edge in vertices.split(' ')])
        gph.add_edge(Edge(*vertices))
    return gph


def main():
    choice = None

    def main_case(param):
        x = int(param)
        if x == 1:
            print('Insert max vertex index for your graph (remember that indexes start from 0):')
            n = int(input('> '))
            gph = g.Graph(n)
            gph = read_edges(gph)
            gph.print()
        elif x == 2:
            graph = create_test_graph()
            g.print_bfs(graph, 1)
            del graph
        elif x == 3:
            graph = create_test_graph()
            g.print_dfs(graph, 1)
            del graph
        else:
            print('No such option!')

    while True:
        view()
        print('Choice:')
        choice = input('> ')
        if choice == 'q':
            break
        main_case(choice)
        print()


if __name__ == '__main__':
    main()