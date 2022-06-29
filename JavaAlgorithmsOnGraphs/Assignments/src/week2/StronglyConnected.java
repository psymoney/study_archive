package week2;

/*
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
*/

import java.util.ArrayList;
import java.util.Scanner;

public class StronglyConnected {
    private static int numberOfStronglyConnectedComponents(ArrayList<Integer>[] adj) {
        //write your code here
        return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        ArrayList<Integer>[] adj = (ArrayList<Integer>[])new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) {
            int x, y;
            x = scanner.nextInt();
            y = scanner.nextInt();
            adj[x - 1].add(y - 1);
        }
        System.out.println(numberOfStronglyConnectedComponents(adj));
    }
}

