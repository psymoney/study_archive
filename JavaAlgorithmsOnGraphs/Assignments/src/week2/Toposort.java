package week2;

/*
## Determining an Order of Courses

# Problem Introduction
    Now, when you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to
    find an order of all courses that is consistent with all dependencies. For this, you find a topological ordering
    of the corresponding directed graph.

# Problem Description
    Task.           Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.
    Input Format.   A graph is given in the standard format.
    Constraints.    1 ≤ 𝑛 ≤ 105, 0 ≤ 𝑚 ≤ 105. The given graph is guaranteed to be acyclic.
    Output Format.  Output any topological ordering of its vertices. (Many DAGs have more than just one
                    topological ordering. You may output any of them.)

# Sample 1.
Input:
4 3
1 2
4 1
3 1
Output:
4 3 1 2

# Sample 2.
Input:
4 1
3 1
Output:
2 3 1 4

# Sample 3.
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
5 4 3 2 1
*/

import java.util.ArrayList;
import java.util.Scanner;

public class Toposort {
    private static ArrayList<Integer> toposort(ArrayList<Integer>[] adj) {
        int used[] = new int[adj.length];
        ArrayList<Integer> order = new ArrayList<Integer>();
        //write your code here
        return order;
    }

    private static void dfs(ArrayList<Integer>[] adj, int[] used, ArrayList<Integer> order, int s) {
      //write your code here
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
        ArrayList<Integer> order = toposort(adj);
        for (int x : order) {
            System.out.print((x + 1) + " ");
        }
    }
}

