"""
## Checking Consistency of CS Curriculum

# Problem Introduction
    A Computer Science curriculum specifies the prerequisites for each course as a list of courses that should be
    taken before taking this course. You would like to perform a consistency check of the curriculum, that is,
    to check that there are no cyclic dependencies. For this, you construct the following directed graph: vertices
    correspond to courses, there is a directed edge (𝑢, 𝑣) is the course 𝑢 should be taken before the course 𝑣.
    Then, it is enough to check whether the resulting graph contains a cycle.

# Problem Description
    Task.           Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.
    Input Format.   A graph is given in the standard format.
    Constraints.    1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑚 ≤ 103.
    Output Format.  Output 1 if the graph contains a cycle and 0 otherwise.

# Sample 1
Input:
4 4
1 2
4 1
2 3
3 1

Output:
1

# Sample 2
Input:
5 7
1 2
2 3
1 3
3 4
1 4
2 5
3 5

Output:
0
"""

import sys

def dfs(adj, used, order, x):
    #write your code here
    pass


def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

