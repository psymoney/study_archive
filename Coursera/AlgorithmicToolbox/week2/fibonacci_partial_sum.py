#### Last Digit of the Sum of Fibonacci Numbers Again
### Problem Description
## Task. Given two non-negative integers m and n, where m<=n, find the last digit of the sum F(m) + F(m+1) + ... + F(n).
## Input Format. The input consists of two non-negative integers m and n separated by a space.
## Constraints. 0<=m<n<=10**14.
## Output Format. Output the last digit of F(m) + F(m+1) + ... + F(n).

import sys


def fibonacci_partial_sum_naive(from_, to):
    sum_to_to = fibonacci_sum_naive(to)
    sum_to_from = 0 if from_ == 0 else fibonacci_sum_naive(from_-1)

    if sum_to_to > sum_to_from:
        return (10 + sum_to_to - sum_to_from) % 10
    else:
        return (sum_to_to - sum_to_from) % 10


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    pattern = find_pattern(10)
    quotient_n = n // len(pattern)
    remainder_n = n % len(pattern)
    sum_pattern = 0
    sum_pattern_to_remainder = 0

    for i,e in enumerate(pattern):
        sum_pattern += e
        if i <= remainder_n:
            sum_pattern_to_remainder += e
    sum_pattern_digit = sum_pattern % 10
    sum_digit = sum_pattern_digit * quotient_n % 10
    sum_pattern_to_remainder_digit = sum_pattern_to_remainder % 10

    return (sum_digit + sum_pattern_to_remainder_digit) % 10


def find_pattern(m):
    if m == 1:
        return [0]
    pattern = [0,1]
    prev = 0
    curr = 1

    for i in range(2, m * m + 1):
        temp = prev
        prev = curr
        curr = (prev + temp) % m
        pattern.append(curr)

        if pattern[i-1] == 0 and pattern[i] == 1:
            pattern.pop(i)
            pattern.pop(i-1)
            break

    return pattern


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
