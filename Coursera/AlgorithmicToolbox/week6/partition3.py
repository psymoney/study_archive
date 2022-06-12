"""
## Partitioning Souvenirs
    You and two of your friends have just returned back home after visiting various countries. Now you would
    like to evenly split all the souvenirs that all three of you bought.

# Problem Description
    Input Format.   The first line contains an integer 𝑛. The second line contains integers 𝑣1, 𝑣2, . . . , 𝑣𝑛 separated
                    by spaces.
    Constraints.    1 ≤ 𝑛 ≤ 20, 1 ≤ 𝑣𝑖 ≤ 30 for all 𝑖.
    Output Format.  Output 1, if it possible to partition 𝑣1, 𝑣2, . . . , 𝑣𝑛 into three subsets with equal sums, and
                    0 otherwise.

# Sample 1.
    Input:
        4
        3 3 3 3
    Output:
        0

# Sample 2.
    Input:
        1
        40
    Output:
        0

# Sample 3.
    Input:
        11
        17 59 34 57 17 23 67 1 18 2 59
    Output:
        1
        34 + 67 + 17 = 23 + 59 + 1 + 17 + 18 = 59 + 2 + 57.

# Sample 4.
    Input:
        13
        1 2 3 4 5 5 7 7 8 10 12 19 25
    Output:
        1
        1 + 3 + 7 + 25 = 2 + 4 + 5 + 7 + 8 + 10 = 5 + 12 + 19.

"""
import sys

DEBUG = False


def partition3(A):
    total_weight = sum(weight for weight in A)
    if total_weight % 3 != 0 or total_weight < 3:
        return 0

    count = 0
    target = total_weight // 3
    numbers = len(A)
    values = [[0] * (numbers + 1) for _ in range(target + 1)]

    for i in range(1, target + 1):
        for j in range(1, numbers + 1):
            values[i][j] = values[i][j - 1]
            if A[j - 1] <= i:
                t = values[i - A[j - 1]][j - 1] + A[j - 1]
                if t > values[i][j]:
                    values[i][j] = t
            if values[i][j] == target:
                count += 1

    if count < 3:
        return 0
    else:
        return 1


def test_cases():
    if partition3([3, 3, 3, 3]) == 0:
        print('first test passed')
    else:
        print('first test failed')
        return None

    if partition3([40]) == 0:
        print('second test passed')
    else:
        print('second test failed')
        return None

    if partition3([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]) == 1:
        print('third test passed')
    else:
        print('third test failed')
        return None

    if partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]) == 1:
        print('forth test passed')
    else:
        print('forth test failed')
        return None


if __name__ == '__main__':
    if DEBUG:
        test_cases()
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

