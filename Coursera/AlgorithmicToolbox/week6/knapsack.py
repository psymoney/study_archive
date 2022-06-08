"""
## Maximum Amount of Gold

# Problem Introduction
    You are given a set of bars of gold and your goal is to take as much gold as possible into
    your bag. There is just one copy of each bar and for each bar you can either take it or not
    (hence you cannot take a fraction of a bar).

# Problem Description
    Task.           Given 𝑛 gold bars, find the maximum weight of gold that fits into a bag of capacity 𝑊.
    Input Format.   The first line of the input contains the capacity 𝑊 of a knapsack and the number 𝑛 of bars
                    of gold. The next line contains 𝑛 integers 𝑤0,𝑤1, . . . ,𝑤𝑛−1 defining the weights of the bars of gold.
    Constraints.    1 ≤ 𝑊 ≤ 104; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤0, . . . ,𝑤𝑛−1 ≤ 10^5.
    Output Format.  Output the maximum weight of gold that fits into a knapsack of capacity 𝑊.

# Sample 1.
    Input:
        10 3
        1 4 8
    Output:
        9

# Starter Files
    Starter files contain an implementation of the following greedy strategy: scan the list of given bars of gold
    and add the current bar if it fits into the current capacity (note that, in this problem, all the items have the
    same value per unit of weight, for a simple reason: they are all made of gold). As you already know from the
    lectures, such a greedy move is not safe. You may want to additionally submit a starter file as a solution to
    the grading system to ensure that this greedy algorithm indeed might produce a non-optimal result.

# Solution
    A detailed solution (with Python code) for this challenge is covered in the companion MOOCBook. We
    strongly encourage you to do your best to solve the challenge yourself before looking into the book! There
    are at least three good reasons for this.
        • By solving this challenge, you practice solving algorithmic problems similar to those given at technical
        interviews.
        • The satisfaction and self confidence that you get when passing the grader is priceless =)
        • Even if you fail to pass the grader yourself, the time will not be lost as you will better understand the
        solution from the book and better appreciate the beauty of the underlying ideas.
"""
import sys

DEBUG = False


def optimal_weight(W, w):
    matrix = [[0] * (W + 1) for _ in range(len(w) + 1)]

    for i in range(len(w)):
        for x in range(1, W + 1):
            if x >= w[i]:
                matrix[i][x] = w[i]
                if x >= matrix[i][x] + matrix[i-1][x-matrix[i][x]]:
                    matrix[i][x] = matrix[i][x] + matrix[i-1][x-matrix[i][x]]
                if matrix[i - 1][x] > matrix[i][x]:
                    matrix[i][x] = matrix[i - 1][x]
            elif x >= matrix[i-1][x]:
                matrix[i][x] = matrix[i-1][x]

    if DEBUG:
        for m in matrix:
            print(m)

    return matrix[-2][-1]


def test_case():
    if optimal_weight(10, [1, 4, 8]) == 9:
        print('first test passed')
    else:
        print('first test failed')
        return False

    if optimal_weight(20, [5, 7, 12, 18]) == 19:
        print('second test passed')
    else:
        print('second test failed')
        return False


if __name__ == '__main__':
    if DEBUG:
        test_case()
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
