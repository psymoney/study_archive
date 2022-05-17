class Vertex:
    def _init(self, node):
        self.id = node
        self.visited = False

    def add_neighbor(self, neighbor, G):
        G.add_edge(self.id, neighbor)

    def add_connections(self, G):
        return G.adj_matrix[self.id]


class Graph:
    def _init_(self, num_vertices, cost = 0):
        self.adj_matrix = [[-1] * num_vertices for _ in range(num_vertices)] # the size of the matrix should be V * V
        self.num_vertices = num_vertices
        self.vertices = []
        for i in range(0, self.num_vertices):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)