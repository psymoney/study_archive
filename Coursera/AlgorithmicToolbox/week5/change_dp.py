"""
## Money Change Again

As we already know, a natural greedy strategy for the change problem does not work correctly for any set of
denominations. For example, if the available denominations are 1, 3, and 4, the greedy algorithm will change
6 cents using three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3). Your goal now is
to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.

# Problem Description
Input Format.       Integer money.
Output Format.      The minimum number of coins with denominations 1, 3, 4 that changes money.
Constraints.        1 ≤ money ≤ 103.
"""
import sys
import math


def get_change(m):
    coins = [1, 3, 4]
    da = [0] * (m + 1)

    for i in range(1, m + 1):
        da[i] = math.inf
        for coin in coins:
            if i >= coin:
                num_coins = da[i - coin] + 1
                if num_coins < da[i]:
                    da[i] = num_coins

    return da[m]


def test_cases():
    if get_change(2) == 2:
        print('first case success')
    else:
        print('first case failed')

    if get_change(7) == 2:
        print('second case success')
    else:
        print('second case failed')

    if get_change(34) == 9:
        print('third case success')
    else:
        print('third case failed')


if __name__ == '__main__':
    # test_cases()
    m = int(sys.stdin.read())
    print(get_change(m))
