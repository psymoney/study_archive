# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n < 2:
        return n

    pattern = find_pattern(m)
    index = n % len(pattern)

    return pattern[index]


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
    test_1_result = get_fibonacci_huge_naive(239, 1000)
    test_2_result = get_fibonacci_huge_naive(2816213588, 239)

    if test_1_result != 161:
        return Exception('did not pass the first test case')
    if test_2_result != 151:
        return Exception('did not pass the second test case')
    print('all test cases complete')

if __name__ == '__main__':
    test_cases()
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))


### Problem Description
## Task. Given two integers n and m, output F(n) mod m (that is, the remainder of F(n) when divided by m).
## Input Format. The input consist of two integers n and m given on the same line (seperated by a space).
## Constraints. 1<= n <=10^14, 2<= m <=10^3
##Output Format. Output F(n) mod m.

