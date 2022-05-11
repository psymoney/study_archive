# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for i in range(n - 1):
        temp = previous
        previous = current
        current = temp + previous
        _sum += current

    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
