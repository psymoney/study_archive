# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    i = 2
    n_0 = 0
    n_1 = 1

    for _ in range(n-1):
        temp = n_1
        n_1 = n_0 + n_1
        n_0 = temp

    return n_1


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
