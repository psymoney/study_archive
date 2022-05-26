"""
## Majority Element

# Problem Introduction
Majority rule is a decision rule that selects the alternative which has a majority,
that is, more than half the votes.
Given a sequence of elements 𝑎1, 𝑎2, . . . , 𝑎𝑛, you would like to check whether
it contains an element that appears more than 𝑛/2 times. A naive way to do
this is the following.
```
    MajorityElement(𝑎1, 𝑎2, . . . , 𝑎𝑛):
        for 𝑖 from 1 to 𝑛:
            currentElement ← 𝑎𝑖
            count ← 0
            for 𝑗 from 1 to 𝑛:
            if 𝑎𝑗 = currentElement:
                count ← count + 1
            if count > 𝑛/2:
                return 𝑎𝑖
        return “no majority element”
```
The running time of this algorithm is quadratic. Your goal is to use the divide-and-conquer technique to
design an 𝑂(𝑛 log 𝑛) algorithm.

# Problem Description
Task.           The goal in this code problem is to check whether an input sequence contains a majority element.
Input Format.   The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
                integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints.    1 ≤ 𝑛 ≤ 10^5; 0 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.
Output Format.  Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times,
                and 0 otherwise.
"""
import sys


def get_majority_element(a, left, right):
    if left >= right:
        return a[left]

    mid = (left + right) // 2
    majority = (right - left + 1) // 2
    left_major = get_majority_element(a, left, mid)
    right_major = get_majority_element(a, mid + 1, right)
    if left_major == right_major:
        return left_major

    if a[left:right+1].count(left_major) > majority:
        return left_major
    elif a[left:right+1].count(right_major) > majority:
        return right_major
    else:
        return -1


def test_cases():
    if get_majority_element([2,3,9,2,2], 0, 4) != 1:
        print('first test success')
    else:
        print('first test failed')

    if get_majority_element([1,2,3,4], 0, 3) == -1:
        print('second test success')
    else:
        print('second test failed')

    if get_majority_element([512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772], 0, 9) == -1:
        print('third test success')
    else:
        print('third test failed')


if __name__ == '__main__':
    # test_cases()
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
