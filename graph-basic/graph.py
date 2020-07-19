from linked_list import LinkedList


class Vertex:
    def __init__(self, value: LinkedList, state=None, next=None):
        self.value = LinkedList(value)
        self.state = state
        self.next = next

class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class Graph:

    def __init__(self, vertex=None, edge=None):
        self.vertex = set(Vertex(vertex))
        self.edge = set(Edge(edge))

    def add_vertex(self, v: Vertex):
        self.vertex.add(v)
        return self.vertex

    def add_edge(self, a: tuple):

