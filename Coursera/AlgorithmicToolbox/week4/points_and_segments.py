"""
## Organizing a Lottery

# Problem Introduction

You are organizing an online lottery. To participate, a person bets on a single
integer. You then draw several ranges of consecutive integers at random.
A participant’s payoff then is proportional to the number of ranges that
contain the participant’s number minus the number of ranges that does not
contain it. You need an efficient algorithm for computing the payoffs for all
participants. A naive way to do this is to simply scan, for all participants, the
list of all ranges. However, you lottery is very popular: you have thousands
of participants and thousands of ranges. For this reason, you cannot afford
a slow naive algorithm.

# Problem Description

Task.           You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
                each point, the number of segments that contain this point.
Input Format.   The first line contains two non-negative integers 𝑠 and 𝑝 defining the number of segments
                and the number of points on a line, respectively. The next 𝑠 lines contain two integers 𝑎𝑖
                , 𝑏𝑖 defining the 𝑖-th segment [𝑎𝑖, 𝑏𝑖].
                The next line contains 𝑝 integers defining points 𝑥1, 𝑥2, . . . , 𝑥𝑝.
Constraints.    1 ≤ 𝑠, 𝑝 ≤ 50000; −10^8 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 10^8 for all 0 ≤ 𝑖 < 𝑠;
                −10^8 ≤ 𝑥𝑗 ≤ 10^8 for all 0 ≤ 𝑗 < 𝑝.
Output Format.  Output 𝑝 non-negative integers 𝑘0, 𝑘1, . . . , 𝑘𝑝−1 where 𝑘𝑖 is the number of segments which contain 𝑥𝑖.
                More formally, 𝑘𝑖 = |{𝑗 : 𝑎𝑗 ≤ 𝑥𝑖 ≤ 𝑏𝑗}| .
'''
Sample 1.
    Input:
        2 3
        0 5
        7 10
        1 6 11
    Output:
        1 0 0

Here, we have two segments and three points. The first point lies only in the first segment while the
remaining two points are outside of all the given segments.

Sample 2.
    Input:
        1 3
        -10 10
        -100 100 0
    Output:
        0 0 1

Sample 3.
    Input:
        3 2
        0 5
        -3 2
        7 10
        1 6
    Output:
        2 0
"""
import sys
import random

LEFT, POINT, RIGHT = 1, 2, 3
DEBUG = False


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    axis_list = []
    point_map = {}
    # arrange each segments and points in an array for sorting
    for e in starts:                                # O(n)
        axis_list.append([e, LEFT])
    for e in ends:                                  # O(n)
        axis_list.append([e, RIGHT])
    for i, e in enumerate(points):                  # O(n)
        axis_list.append([e, POINT])
        if e not in point_map:
            point_map[e] = [i]
        else:
            point_map[e].append(i)

    sa = sorted(axis_list, key=lambda e: (e[0], e[1]))
    # quick_sort(axis_list, 0, len(axis_list) - 1)
    if DEBUG:
        print(f'result = {sa}')

    queue = []
    for item in sa:              # O(3n)
        if item[1] == 1:
            queue.append(item)
        elif item[1] == 2:
            i = point_map[item[0]]
            for j in i:
                cnt[j] = len(queue)
        elif item[1] == 3:
            queue.pop(len(queue) - 1)

    if DEBUG:
        print(f'cnt = {cnt}')
    return cnt


def quick_sort(array, left, right):
    if left >= right:
        return

    mid = random.randint(left, right)
    array[left], array[mid] = array[mid], array[left]

    lt, rt = partition(array, left, right)

    quick_sort(array, left, lt - 1)
    quick_sort(array, rt + 1, right)


def partition(a, l, r):
    i = l
    while i <= r:
        if a[i][0] == a[l][0]:
            # if a[l][1] < a[i][1]:
            #     pass
            # if a[l][1] == a[i][1]:
            #     pass
            if a[l][1] > a[i][1]:
                a[l], a[i] = a[i], a[l]
            i += 1
        elif a[i][0] < a[l][0]:
            a[i], a[l] = a[l], a[i]
            i += 1
            l += 1
        elif a[i][0] > a[l][0]:
            a[i], a[r] = a[r], a[i]
            r -= 1
    return l, r


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def test_cases():
    fast_count_segments([0, 7],[5, 10],[1, 6, 11])
    fast_count_segments([-10],[10],[-100, 100, 0])
    fast_count_segments([0, -3, 7],[5, 2, 10],[1, 6])


if __name__ == '__main__':
    if DEBUG:
        test_cases()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
