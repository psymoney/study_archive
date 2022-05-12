# Uses python3
import sys


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


def test_cases():
    test_1_result = fibonacci_sum_naive(3)
    test_2_result = fibonacci_sum_naive(100)

    if test_1_result != 4:
        print('first case went wrong')
    if test_2_result != 5:
        print('second case went wrong')
    print('all test cases complete')


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
