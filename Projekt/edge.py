class Edge:
    """Class represents edge in graph from vertice1 to vertice2"""


    def __init__(self, val1, val2):
        if val1 < 0 or val2 < 0:
            raise ValueError('Vertices can\'t be negative numbers')
        self.v1 = val1
        self.v2 = val2


    def __str__(self):
        return "({}->{})".format(self.v1, self.v2)

    def __eq__(self, other):
        return self.v1 == other.v1 and self.v2 == other.v2