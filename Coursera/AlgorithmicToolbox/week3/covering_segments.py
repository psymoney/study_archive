"""
Collecting Signatures

Problem Description
Task.   Given a set of 𝑛 segments {[𝑎0, 𝑏0], [𝑎1, 𝑏1], . . . , [𝑎𝑛−1, 𝑏𝑛−1]} with integer coordinates on a line, find
        the minimum number 𝑚 of points such that each segment contains at least one point. That is, find a
        set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖, 𝑏𝑖] there is a point 𝑥 ∈ 𝑋 such
        that 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.
Input Format.   The first line of the input contains the number 𝑛 of segments. Each of the following 𝑛 lines
        contains two integers 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th
        segment.
Constraints.    1 ≤ 𝑛 ≤ 100; 0 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.
Output Format.  Output the minimum number 𝑚 of points on the first line and the integer coordinates
        of 𝑚 points (separated by spaces) on the second line. You can output the points in any order. If there
        are many such sets of points, you can output any set. (It is not difficult to see that there always exist
        a set of points of the minimum size such that all the coordinates of the points are integers.)
"""

import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    count = 0
    points = []
    i = 0
    while i < len(segments):
        point = segments[i][1]
        for j in range(i+1, len(segments)):
            if point < segments[j][0]:
                points.append(point)
                break
            i += 1
    print(points)
    return points


def test_cases():
    if optimal_points([[1,3], [2,5], [3,6]]) != [1,3]:
        print('first test success')
    else:
        print('first test failed')


if __name__ == '__main__':
    test_cases()
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
