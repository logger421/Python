import threading
import time

import graph as g
from edge import Edge


def read_edges(gph: g.Graph):
    print("Insert your graph's edges or type 'q' to quit")
    print('Enter pair of integers (space separated):')
    vertices = None
    while True:
        try:
            vertices = input('> ')
            if vertices == 'q': break
            vertices = tuple([int(edge) for edge in vertices.split(' ')])
            gph.add_edge(Edge(*vertices))
        except ValueError:
            print('Vertex index is greater then declared max vertex index in graph')
        else:
            continue
    return gph


def create_test_graph():
    return g.Graph.load_from_file('demo.txt')


def view():
    i = 35
    print('-' * i)
    print("Select one of options: ")
    print('-' * i)
    print('1) Create graph')
    print('2) Bfs example')
    print('3) Dfs example')
    print('4) Load from file')
    print("Type 'q' to exit")
    print('-' * i)


def sub_view():
    i = 35
    print('-' * i)
    print("Select one of options: ")
    print('-' * i)
    print('1) print BFS')
    print('2) print DFS')
    print('3) print graph')
    print('4) save to file')
    print("Type 'q' to go back")
    print('-' * i)


def sub_case(param, instance: g.Graph):
    param = int(param)
    if param == 1:
        g.print_bfs(instance, 1)
        print()
    elif param == 2:
        g.print_dfs(instance, 1)
        print()
    elif param == 3:
        instance.print()
    elif param == 4:
        print('Insert file name to save graph')
        file_name = str(input('> '))
        g.Graph.save_to_file(instance, file_name)
        threading.Thread(target=g.Graph.save_to_file(instance, file_name)).start()
    else:
        print('No such option!')


def main_case(param):
    x = int(param)
    if x == 1:
        print('Insert max vertex index for your graph (remember that indexes start from 0):')
        while True:
            try:
                n = int(input('> '))
                print('Type "True" if your graph is directed or "False" if undirected')
                is_directed = eval(input('> '))
            except ValueError:
                print("Please, enter a valid value")
                continue
            else:
                break
        gph = g.Graph(n, is_directed)
        gph = read_edges(gph)
        while True:
            sub_view()
            print('Choice:')
            sub_choice = input('> ')
            if sub_choice == 'q':
                break
            sub_case(sub_choice, gph)
            input("Press Enter to continue...")
        del gph
    elif x == 2:
        graph = create_test_graph()
        g.print_bfs(graph, 1)
        print()
        del graph
    elif x == 3:
        graph = create_test_graph()
        g.print_dfs(graph, 1)
        print()
        del graph
    elif x == 4:
        print('Insert file name to load graph')
        file_name = str(input('> '))
        graph = g.Graph.load_from_file(file_name)
        print('loading data...')
        time.sleep(1)
        while True:
            sub_view()
            print('Choice:')
            sub_choice = input('> ')
            if sub_choice == 'q':
                break
            sub_case(sub_choice, graph)
            input("Press Enter to continue...")
        del graph
    else:
        print('No such option!')


def main():
    choice = None
    while True:
        view()
        print('Choice:')
        choice = input('> ')
        if choice == 'q':
            break
        main_case(choice)
        input("Press Enter to continue...")
        print()


if __name__ == '__main__':
    main()
