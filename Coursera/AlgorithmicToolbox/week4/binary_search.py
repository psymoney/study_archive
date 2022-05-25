"""
## Binary Search

# Problem Introduction
In this problem, you will implement the binary search algorithm that allows searching
very efficiently (even huge) lists, provided that the list is sorted.

# Problem Description
Task.           The goal in this code problem is to implement the binary search algorithm.
Input Format.   The first two lines of the input contain an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < · · · < 𝑎𝑛−1
                of 𝑛 distinct positive integers in increasing order. The next two line contain an integer 𝑘 and 𝑘 positive
                integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.
Constraints.    1 ≤ 𝑘 ≤ 10^5; 1 ≤ 𝑛 ≤ 3 · 10^4; 1 ≤ 𝑎𝑖 ≤ 10^9
                for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏𝑗 ≤ 10^9
                for all 0 ≤ 𝑗 < 𝑘;
Output Format.  For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎𝑗 = 𝑏𝑖 or −1 if there
                is no such index.
"""


def binary_search(keys, query):

    def search_in_binary(array, left, right, q):
        center = (left + right) // 2
        if array[center] == q:
            return center

        if left >= right:
            return -1

        if q > array[center]:
            return search_in_binary(array, center + 1, right, q)
        elif q < array[center]:
            return search_in_binary(array, left, center - 1, q)

    return search_in_binary(keys, 0, len(keys)-1, query)


def test_cases():
    first_answer = []
    for e in [8, 1, 23, 1, 11]:
        first_answer.append(binary_search([1, 5, 8, 12, 13], e))

    if first_answer == [2, 0, -1, 0, -1]:
        print('first case success')
    else:
        print('first case failed')


if __name__ == '__main__':
    # test_cases()
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
