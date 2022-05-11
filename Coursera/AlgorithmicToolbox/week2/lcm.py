# Uses python3
import sys


def gcd_naive(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return a


def lcm_naive(a, b):
    gcd = gcd_naive(a, b)
    return int((a * b) / gcd)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

