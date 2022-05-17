"""
## Maximum Advertisement Revenue

# Problem Introduction
You have 𝑛 ads to place on a popular Internet page. For each ad, you know how
much is the advertiser willing to pay for one click on this ad. You have set up 𝑛
slots on your page and estimated the expected number of clicks per day for each
slot. Now, your goal is to distribute the ads among the slots to maximize the
total revenue.

# Problem Description
Task.   Given two sequences 𝑎1, 𝑎2, . . . , 𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1, 𝑏2, . . . , 𝑏𝑛 (𝑏𝑖 is
        the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖, 𝑏𝑗)
        such that the sum of their products is maximized.
Input Format.   The first line contains an integer 𝑛, the second one contains a sequence of integers
        𝑎1, 𝑎2, . . . , 𝑎𝑛, the third one contains a sequence of integers 𝑏1, 𝑏2, . . . , 𝑏𝑛.
Constraints.    1 ≤ 𝑛 ≤ 10^3; −10^5 ≤ 𝑎𝑖, 𝑏𝑖 ≤ 10^5 for all 1 ≤ 𝑖 ≤ 𝑛.
Output Format.  Output the maximum value of Σ𝑛𝑖=1𝑎𝑖𝑐𝑖, where 𝑐1, 𝑐2, . . . , 𝑐𝑛 is a permutation of 𝑏1, 𝑏2, . . . , 𝑏𝑛.
"""
import sys


def max_dot_product(a, b):
    revenue = 0
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(len(a)):
        revenue += a[i] * b[i]
    return revenue


def test_cases():
    if max_dot_product([23], [39]) == 897:
        print('first case success')
    else:
        print('first case failed')
    if max_dot_product([1, 3, -5],[-2, 4, 1]) == 23:
        print('second case success')
    else:
        print('second case failed')


if __name__ == '__main__':
    # test_cases()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
