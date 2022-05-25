"""
## Maximum Number of Prizes

# Problem Introduction
You are organizing a funny competition for children. As a prize fund you have 𝑛
candies. You would like to use these candies for top 𝑘 places in a competition
with a natural restriction that a higher place gets a larger number of candies.
To make as many children happy as possible, you are going to find the largest
value of 𝑘 for which it is possible.

# Problem Description
Task. The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise
    distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
    𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 ̸= 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.
Input Format. The input consists of a single integer 𝑛.
Constraints. 1 ≤ 𝑛 ≤ 10^9.
Output Format. In the first line, output the maximum number 𝑘 such that 𝑛 can be represented as a sum
    of 𝑘 pairwise distinct positive integers. In the second line, output 𝑘 pairwise distinct positive integers
    that sum up to 𝑛 (if there are many such representations, output any of them).
"""
import sys


def optimal_summands(n):
    summands = []
    i = 1
    sum = 0
    while sum + i <= n:
        if n-sum-i > i:
            summands.append(i)
        else:
            summands.append(n - sum)
        sum += i
        i += 1
    return summands


def test_cases():
    if optimal_summands(6) == [1, 2, 3]:
        print('first case success')
    else:
        print('first case failed')

    if optimal_summands(8) == [1, 2, 5]:
        print('second case success')
    else:
        print('second case failed')

    if optimal_summands(2) == [2]:
        print('third case success')
    else:
        print('third case failed')


if __name__ == '__main__':
    # test_cases()
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
