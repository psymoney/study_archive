"""
## Primitive Calculator

# Problem Introduction
You are given a primitive calculator that can perform the following three operations with
the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a
positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛
starting from the number 1.

# Problem Description
Task.           Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛
                starting from the number 1.
Input Format.   The input consists of a single integer 1 ≤ 𝑛 ≤ 106.
Output Format.  In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1.
                In the second line output a sequence of intermediate numbers. That is, the second line should contain
                positive integers 𝑎0, 𝑎2, . . . , 𝑎𝑘−1 such that 𝑎0 = 1, 𝑎𝑘−1 = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, 𝑎𝑖+1 is equal to
                either 𝑎𝑖 + 1, 2𝑎𝑖, or 3𝑎𝑖. If there are many such sequences, output any one of them.
"""
import math
import sys

DEBUG = False


def optimal_sequence(n):
    sequence = [0] * (n + 1)
    operators = [None] * (n + 1)
    result = []

    if n == 1:
        return [1]

    for i in range(2, n + 1):
        num_operations = math.inf
        operator = ''
        if sequence[i - 1] + 1 < num_operations:
            num_operations = sequence[i - 1] + 1
            operator = '+1'
        if i % 2 == 0 and sequence[i // 2] < num_operations:
            num_operations = sequence[i // 2] + 1
            operator = '*2'
        if i % 3 == 0 and sequence[i // 3] < num_operations:
            num_operations = sequence[i // 3] + 1
            operator = '*3'
        sequence[i] = num_operations
        operators[i] = operator

    result.append(n)
    i = n
    while i > 1:
        operator = operators[i]

        if operator == '+1':
            i = i - 1
        elif operator == '*2':
            i = i // 2
        elif operator == '*3':
            i = i // 3
        result.append(i)
    result.reverse()
    if DEBUG:
        print(result)

    return result


def test_cases():
    if optimal_sequence(1) == [1]:
        print('first test success')
    else:
        print('first test failed')

    if optimal_sequence(5) == [1, 2, 4, 5]:
        print('second test success')
    else:
        print('second test failed')

    if optimal_sequence(96234) == [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]:
        print('third test success')
    else:
        print('third test failed')


if __name__ == '__main__':
    if DEBUG:
        test_cases()
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
