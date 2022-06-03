# Uses python3
import sys
import math


def get_change(m):
    denominations = [1, 3, 4]
    da = [0] * (m + 1)

    for i in range(1, m + 1):
        a = i // denominations[0] if i % denominations[0] == 0 else math.inf
        b = i // denominations[1] if i % denominations[1] == 0 else math.inf
        c = i // denominations[2] if i % denominations[2] == 0 else math.inf
        print(f'i = {i} da[i-1] = {da[i-1]} a = {a}, b = {b}, c = {c}')
        da[i] = min(da[i-1] + 1, a, b, c)
    print(da)
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
    test_cases()
    m = int(sys.stdin.read())
    print(get_change(m))
