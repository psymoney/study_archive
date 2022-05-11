# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        temp = previous
        previous = current
        current = temp + previous

    return current % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
