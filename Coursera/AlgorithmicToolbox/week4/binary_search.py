"""
## Binary Search

# Problem Introduction
In this problem, you will implement the binary search algorithm that allows searching
very efficiently (even huge) lists, provided that the list is sorted.

# Problem Description
Task.           The goal in this code problem is to implement the binary search algorithm.
Input Format.   The first two lines of the input contain an integer ๐ and a sequence ๐0 < ๐1 < ยท ยท ยท < ๐๐โ1
                of ๐ distinct positive integers in increasing order. The next two line contain an integer ๐ and ๐ positive
                integers ๐0, ๐1, . . . , ๐๐โ1.
Constraints.    1 โค ๐ โค 10^5; 1 โค ๐ โค 3 ยท 10^4; 1 โค ๐๐ โค 10^9
                for all 0 โค ๐ < ๐; 1 โค ๐๐ โค 10^9
                for all 0 โค ๐ < ๐;
Output Format.  For all ๐ from 0 to ๐ โ 1, output an index 0 โค ๐ โค ๐ โ 1 such that ๐๐ = ๐๐ or โ1 if there
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
