"""
## Finding an Exit from a Maze

# Problem Introduction
    A maze is a rectangular grid of cells with walls between some of adjacent cells.
    You would like to check whether there is a path from a given cell to a given
    exit from a maze where an exit is also a cell that lies on the border of the maze
    (in the example shown to the right there are two exits: one on the left border
    and one on the right border). For this, you represent the maze as an undirected
    graph: vertices of the graph are cells of the maze, two vertices are connected by
    an undirected edge if they are adjacent and there is no wall between them. Then,
    to check whether there is a path between two given cells in the maze, it suffices to
    check that there is a path between the corresponding two vertices in the graph.

# Problem Description
    Task.           Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.
                    Input Format. An undirected graph with 𝑛 vertices and 𝑚 edges. The next line contains two vertices 𝑢
                    and 𝑣 of the graph.
    Constraints.    2 ≤ 𝑛 ≤ 103; 1 ≤ 𝑚 ≤ 103; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 𝑢 ̸= 𝑣.
    Output Format.  Output 1 if there is a path between 𝑢 and 𝑣 and 0 otherwise.

# Sample 1.
    Input:
        4 4
        1 2
        3 2
        4 3
        1 4
        1 4
    Output:
        1

# Sample 2.
    Input:
        4 2
        1 2
        3 2
        1 4
    Output:
        0
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


def travel_from_to(_from, _to):
    stack = []

    stack.append(_from)

    while len(stack) > 0:
        curr_node = stack.pop(len(stack) - 1)
        if curr_node == _to:
            return 1
        if curr_node.visited:
            continue # check if continue works
        curr_node.visited = True
        for node in curr_node.adjacent_nodes:
            stack.append(node)

    return 0


def reach(adj, x, y):
    graph = []

    for i in range(1, len(adj) + 1):
        graph.append(Node(i))

    for i in range(len(graph)):
        for j in range(len(adj[i])):
            graph[i].set_adjacent_node(graph[adj[i][j]])

    return travel_from_to(graph[x], graph[y])


def test_cases():
    if reach([[1, 3], [0, 2], [1, 3], [2, 0]], 0, 3) == 1:
        print('first case passed')
    else:
        print('first case failed')
        return None

    if reach([[1], [0, 2], [1], []], 0, 3) == 0:
        print('second case passed')
    else:
        print('second case failed')
        return None


if __name__ == '__main__':
    if DEBUG:
        test_cases()

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
