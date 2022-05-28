"""
## Number of Inversions

# Problem Introduction

An inversion of a sequence 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such
that 𝑎𝑖 > 𝑎𝑗 . The number of inversions of a sequence in some sense measures how
close the sequence is to being sorted. For example, a sorted (in non-descending
order) sequence contains no inversions at all, while in a sequence sorted in descending order any two elements constitute an inversion (for a total of 𝑛(𝑛 − 1)/2
inversions).

# Problem Description

Task.           The goal in this problem is to count the number of inversions of a given sequence.
Input Format.   The first line contains an integer 𝑛, the next one contains a sequence of integers
                𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints.    1 ≤ 𝑛 ≤ 10^5, 1 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.
Output Format.  Output the number of inversions in the sequence.

# What To Do

This problem can be solved by modifying the merge sort algorithm. For this, we change both the Merge and
MergeSort procedures as follows:
    • Merge(𝐵, 𝐶) returns the resulting sorted array and the number of pairs (𝑏, 𝑐) such that 𝑏 ∈ 𝐵, 𝑐 ∈ 𝐶, and 𝑏 > 𝑐;
    • MergeSort(𝐴) returns a sorted array 𝐴 and the number of inversions in 𝐴.

"""
import sys
import time


DEBUG = False


def merge(a, b):
    merged_array = []
    cnt = 0
    # for i in range(len(a)):
    #     for j in range(len(b)):
    #         if a[i] > b[j]:
    #             cnt += 1
    #             continue
    #         if a[i] <= b[j]:
    #             break

    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged_array.append(a[i])
            i += 1
            # if a[i-1] is smaller than b[j], then a[i] is bigger for all b[0], ..., b[j-1]
            # so the number of inversions with a[i] and b[0], ..., b[j-1] is j
            if j > 0 and i < len(a):
                cnt += j
                # if a[i-1] is smaller than b[j], a[i] needs to compare with b[0], ..., b[j-1]
                # for c in range(0, j):
                #     if a[i] > b[c]:
                #         cnt += 1
                #         if DEBUG:
                #             print(f'a = {a}, b = {b}, i = {i}, j = {j}, cnt = {cnt}, c = {c}')
        elif b[j] < a[i]:
            merged_array.append(b[j])
            j += 1
            cnt += 1
            if DEBUG:
                print(f'a = {a}, b = {b}, i = {i}, j = {j}, cnt = {cnt}')

    if i != len(a):
        merged_array += a[i:]
        # if iteration of b is finished before array a's iteration is finished, then all element of b is smaller than
        # a[i] for all 0 < i < len(a) - 1
        # so the number of inversions with array a[i:] and b is (len(a) - i) * len(b)
        i += 1
        cnt += (len(a) - i) * len(b)
        # for c in range(i, len(a)):
        #     for d in range(len(b)):
        #         if a[c] > b[d]:
        #             cnt += 1
        #             if DEBUG:
        #                 print(f'a = {a}, b = {b}, i = {i}, j = {j}, cnt = {cnt}, c = {c}, d = {d}')
        #             continue
        #         else:
        #             break
    if j != len(b):
        merged_array += b[j:]

    return merged_array, cnt


def merge_sort(array, l, r):
    if l >= r:
        return [array[l]], 0

    mid = (l + r) // 2

    a, cnt_a = merge_sort(array, l, mid)
    b, cnt_b = merge_sort(array, mid + 1, r)

    sorted_array, inversion_cnt = merge(a, b)
    inversion_cnt += cnt_a + cnt_b
    return sorted_array, inversion_cnt


def get_number_of_inversions(a, b, left, right):
    cnt = 0
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            cnt += 1

    if DEBUG:
        print(f'cnt = {cnt}')

    if cnt == len(a) - 1:
        if DEBUG:
            print(f'result = {(len(a)) * (len(a) - 1) // 2}')
        return (len(a)) * (len(a) - 1) // 2

    sorted_array, number_of_inversions = merge_sort(a, left, right - 1)
    return number_of_inversions


def test_cases():
    array = [9, 8, 7, 3, 2, 1]
    cnt = get_number_of_inversions(array, [], 0, len(array) - 1)

    print(f'cnt = {cnt}')


if __name__ == '__main__':
    if DEBUG:
        run_time = round(time.time() * 1000)
        test_cases()
        print(round(time.time() * 1000) - run_time)
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
