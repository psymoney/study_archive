# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    previous = 0
    current  = 1

    if from_ < 2:
        _sum += 1

    for i in range(2, to + 1):
        temp = previous
        previous = current
        current = temp + previous

        if i >= from_:
            _sum += current
    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
