"""
## Improving Quick Sort

# Problem Introduction

The goal in this problem is to redesign a given implementation of the randomized
quick sort algorithm so that it works fast even on sequences containing
many equal elements.

#Problem Description

Task.           To force the given implementation of the quick sort algorithm to efficiently process sequences with
                few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new
                partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.
Input Format.   The first line of the input contains an integer 𝑛. The next line contains a sequence of 𝑛
                integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints.    1 ≤ 𝑛 ≤ 10^5; 1 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.
Output Format.  Output this sequence sorted in non-decreasing order.
"""
import sys
import random


def partition3(a, l, r):
    i = l
    while i <= r:
        if a[i] == a[l]:
            i += 1
        elif a[i] < a[l]:
            a[i], a[l] = a[l], a[i]
            i += 1
            l += 1
        elif a[i] > a[l]:
            a[i], a[r] = a[r], a[i]
            r -= 1
    return l, r


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    lt, rt = partition3(a, l, r)
    randomized_quick_sort(a, l, lt - 1);
    randomized_quick_sort(a, rt + 1, r);


def test_cases():
    array = [2,3,9,2,2]
    randomized_quick_sort(array, 0, len(array) - 1)
    if array == [2, 2, 2, 3, 9]:
        print('first case success')
    else:
        print('first case failed')

    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    randomized_quick_sort(array, 0, len(array) - 1)
    if array == [1,2,3,4,5,6,7,8,9,10]:
        print('second case success')
    else:
        print('second case failed')


if __name__ == '__main__':
    # test_cases()
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
