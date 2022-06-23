"""
## Checking Whether Any Intersection in a City is Reachable from Any Other

# Problem Introduction
    The police department of a city has made all streets one-way. You would like
    to check whether it is still possible to drive legally from any intersection to
    any other intersection. For this, you construct a directed graph: vertices are
    intersections, there is an edge (𝑢, 𝑣) whenever there is a (one-way) street from
    𝑢 to 𝑣 in the city. Then, it suffices to check whether all the vertices in the
    graph lie in the same strongly connected component.

# Problem Description
    Task.           Compute the number of strongly connected components of a given directed graph with 𝑛 vertices and
                    𝑚 edges.
    Input Format.   A graph is given in the standard format.
    Constraints.    1 ≤ 𝑛 ≤ 104, 0 ≤ 𝑚 ≤ 104.
    Output Format.  Output the number of strongly connected components.

# Sample 1.
Input:
4 4
1 2
4 1
2 3
3 1
Output:
2

# Sample 2.
Input:
5 7
2 1
3 2
3 1
4 3
4 1
5 2
5 3
Output:
5
"""

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
