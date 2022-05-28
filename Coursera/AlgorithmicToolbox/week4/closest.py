"""
## Closest Points

# Problem Introduction

In this problem, your goal is to find the closest pair of points among the given 𝑛
points. This is a basic primitive in computational geometry having applications in,
for example, graphics, computer vision, traffic-control systems.

# Problem Description

Task.           Given 𝑛 points on a plane, find the smallest distance between a pair of two (different) points. Recall
                that the distance between points (𝑥1, 𝑦1) and (𝑥2, 𝑦2) is equal to √︀((𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2).
Input Format.   The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point (𝑥𝑖, 𝑦𝑖).
Constraints.    2 ≤ 𝑛 ≤ 10^5; −10^9 ≤ 𝑥𝑖, 𝑦𝑖 ≤ 10^9 are integers.
Output Format.  Output the minimum distance. The absolute value of the difference between the answer
                of your program and the optimal value should be at most 10−3. To ensure this, output your answer
                with at least four digits after the decimal point (otherwise your answer, while being computed correctly,
                can turn out to be wrong because of rounding issues).
```
Sample 1.
    Input:
        2
        0 0
        3 4
    Output:
        5.0

There are only two points here. The distance between them is 5.

Sample 2.
    Input:
        4
        7 7
        1 100
        4 8
        7 7
    Output:
        0.0

There are two coinciding points among the four given points. Thus, the minimum distance is zero.

Sample 3.
    Input:
        11
        4 4
        -2 -2
        -3 -4
        -1 3
        2 3
        -4 0
        1 1
        -1 -1
        3 -1
        -4 2
        -2 4
    Output:
        1.414213

The smallest distance is √2. There are two pairs of points at this distance: (−1, −1) and (−2, −2);
(−2, 4) and (−1, 3).
```
"""
import sys
import math

DEBUG = True


def minimum_distance(x, y):
    #write your code here
    return 10 ** 18


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
