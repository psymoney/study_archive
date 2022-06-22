"""
## Adding Exits to a Maze

# Problem Introduction
    Now you decide to make sure that there are no dead zones in a maze, that is, that at least one exit is
    reachable from each cell. For this, you find connected components of the corresponding undirected graph
    and ensure that each component contains an exit cell.

# Problem Description
    Task.           Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components
                    in it.
    Input Format.   A graph is given in the standard format.
    Constraints.    1 ≤ 𝑛 ≤ 10^3, 0 ≤ 𝑚 ≤ 10^3.
    Output Format.  Output the number of connected components.

# Sample 1.
Input
4 2
1 2
3 2

Output
2


"""
import sys

DEBUG = False


class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.adjacent_nodes = []

    def set_adjacent_node(self, adjacent_node):
        self.adjacent_nodes.append(adjacent_node)

    def traverse(self):
        if self.visited:
            return 0

        stack = []
        stack.append(self)

        while len(stack) > 0:
            curr_node = stack.pop(len(stack) - 1)
            if curr_node.visited:
                continue
            curr_node.visited = True
            for node in curr_node.adjacent_nodes:
                stack.append(node)

        return 1


def number_of_components(adj):
    result = 0
    graph = []

    for i in range(1, len(adj) + 1):
        graph.append(Node(i))

    for i in range(len(graph)):
        for j in range(len(adj[i])):
            graph[i].set_adjacent_node(graph[adj[i][j]])

    for vertex in graph:
        result += vertex.traverse()

    if DEBUG:
        print(f'result = {result}')

    return result


def test_cases():
    if number_of_components([[1], [0, 2], [1], []]) == 2:
        print('first case passed')
    else:
        print('first case failed')
        return None


if __name__ == '__main__':
    if DEBUG:
        test_cases()

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
