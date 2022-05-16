#### Money Change
### Problem Description
## Task. The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10
## Input Format. The input consists of a single integer 𝑚.
## Constraints. 1 ≤ 𝑚 ≤ 10^3
## Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes �

import sys


def get_change(m):
    coins = 0
    denominations = [10, 5, 1]
    for d in denominations:
        coins += m // d
        m = m % d
    return coins


def test_cases():
    if get_change(2) == 2:
        print('first case success')
    else:
        print('first case failed')

    if get_change(28) == 6:
        print('second case success')
    else:
        print('second case failed')


if __name__ == '__main__':
    # test_cases()
    m = int(sys.stdin.read())
    print(get_change(m))
