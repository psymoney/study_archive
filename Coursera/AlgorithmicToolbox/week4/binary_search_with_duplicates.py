"""
## Binary Search with Duplicates

# Problem Description
Task.           Find the first occurence of an integer in the given sorted sequence of integers (possibly with duplicates).
Input Format.   The first two lines of the input contain an integer ๐ and a sequence ๐0 โค ๐1 โค ยท ยท ยท โค ๐๐โ1
                of ๐ positive integers in non-decreasing order. The next two lines contain an integer ๐ and ๐ positive
                integers ๐0, ๐1, . . . , ๐๐โ1.
Constraints.    1 โค ๐ โค 10^5 ; 1 โค ๐ โค 3 ยท 10^4 ;
                1 โค ๐๐ โค 10^9 for all 0 โค ๐ < ๐;
                1 โค ๐๐ โค 10^9 for all 0 โค ๐ < ๐;
Output Format.  For all ๐ from 0 to ๐ โ 1, output an index 0 โค ๐ โค ๐ โ 1 of the first occurrence of ๐๐ (i.e.,
                ๐๐ = ๐๐) or โ1 if there is no such index.
"""


def binary_search(keys, query):
    def search_in_binary_with_duplicates(array, left, right, q):
        center = (left + right) // 2
        if array[center] == q:
            if center == 0:
                return center
            if array[center - 1] == q:
                return search_in_binary_with_duplicates(array, left, center - 1, q)
            return center

        if left >= right:
            return -1

        if q > array[center]:
            return search_in_binary_with_duplicates(array, center + 1, right, q)
        elif q < array[center]:
            return search_in_binary_with_duplicates(array, left, center - 1, q)

    return search_in_binary_with_duplicates(keys, 0, len(keys)-1, query)


def test_cases():
    first_result = []
    for e in [9, 4, 5, 2]:
        first_result.append(binary_search([2, 4, 4, 4, 7, 7, 9], e))
    print(first_result)
    if first_result == [6, 1, -1, 0]:
        print('first test success')
    else:
        print('first test failed')

    second_result = []
    for e in [2]:
        second_result.append(binary_search([2, 2, 2, 2, 2, 2, 2, 2, 2], e))
    print(second_result)
    if second_result == [0]:
        print('second test success')
    else:
        print('second test failed')


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
