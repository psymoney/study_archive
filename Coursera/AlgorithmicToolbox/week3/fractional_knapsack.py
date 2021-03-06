"""
##  Maximum Value of the Loot

# Problem Introduction
A thief finds much more loot than his bag can fit. Help him to find the most valuable combination
of items assuming that any fraction of a loot item can be put into his bag.

# Problem Description
Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
Input Format. The first line of the input contains the number π of items and the capacity π of a knapsack.
        The next π lines define the values and weights of the items. The π-th line contains integers π£π and π€πβthe
        value and the weight of π-th item, respectively
Constraints. 1 β€ π β€ 10^3, 0 β€ π β€ 2 Β· 10^6; 0 β€ π£π β€ 2 Β· 10^6, 0 < π€π β€ 2 Β· 10^6 for all 1 β€ π β€ π. All the numbers are integers.
Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute
        value of the difference between the answer of your program and the optimal value should be at most
        10β3. To ensure this, output your answer with at least four digits after the decimal point (otherwise
        your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
"""

import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    value_per_weight = []
    for i, v in enumerate(values):
        value_per_weight.append(v / weights[i])

    while capacity > 0 and len(value_per_weight) > 0:
        idx = value_per_weight.index(max(value_per_weight))
        if weights[idx] >= capacity:
            value += capacity * value_per_weight[idx]
            capacity = 0
        else:
            value += weights[idx] * value_per_weight[idx]
            capacity -= weights[idx]
        values.pop(idx)
        weights.pop(idx)
        value_per_weight.pop(idx)
    return round(value, 4)


def test_cases():
    if get_optimal_value(50, [20, 50, 30], [60, 100, 120]) == 180.0000:
        print('first case success')
    else:
        print('first case failed')
    if get_optimal_value(100, [30], [500]) == 166.6667:
        print('second case success')
    else:
        print('second case failed')


if __name__ == "__main__":
    # test_cases()
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
