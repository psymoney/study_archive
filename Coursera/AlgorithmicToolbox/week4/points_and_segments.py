"""
## Organizing a Lottery

# Problem Introduction

You are organizing an online lottery. To participate, a person bets on a single
integer. You then draw several ranges of consecutive integers at random.
A participantβs payoff then is proportional to the number of ranges that
contain the participantβs number minus the number of ranges that does not
contain it. You need an efficient algorithm for computing the payoffs for all
participants. A naive way to do this is to simply scan, for all participants, the
list of all ranges. However, you lottery is very popular: you have thousands
of participants and thousands of ranges. For this reason, you cannot afford
a slow naive algorithm.

# Problem Description

Task.           You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
                each point, the number of segments that contain this point.
Input Format.   The first line contains two non-negative integers π  and π defining the number of segments
                and the number of points on a line, respectively. The next π  lines contain two integers ππ
                , ππ defining the π-th segment [ππ, ππ].
                The next line contains π integers defining points π₯1, π₯2, . . . , π₯π.
Constraints.    1 β€ π , π β€ 50000; β10^8 β€ ππ β€ ππ β€ 10^8 for all 0 β€ π < π ;
                β10^8 β€ π₯π β€ 10^8 for all 0 β€ π < π.
Output Format.  Output π non-negative integers π0, π1, . . . , ππβ1 where ππ is the number of segments which contain π₯π.
                More formally, ππ = |{π : ππ β€ π₯π β€ ππ}| .
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
