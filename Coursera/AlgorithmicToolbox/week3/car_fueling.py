#### Car Fueling
### Problem Description
## Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
#  specifies an integer 𝑛. Finally, the last line contains integers stop1 ,stop2, . . . ,stop𝑛.
## Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
#  on a full tank, and there are gas stations at distances stop1,stop2, . . . ,stop𝑛 along the way, output the
#  minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
#  reach the destination, output −1.
## Constraints. 1 ≤ 𝑑 ≤ 10^5. 1 ≤ 𝑚 ≤ 400. 1 ≤ 𝑛 ≤ 300. 0 < stop1 < stop2 < · · · < stop𝑛 < 𝑑.


import sys


def compute_min_refills(distance, tank, stops):
    location = 0
    rest_fuel = tank
    fuel_count = 0
    stops.append(distance)

    curr_stop = location
    while location < distance and len(stops) != 0:
        if stops[0] - location > tank:
            return -1

        if stops[0] - location <= rest_fuel:
            rest_fuel -= (stops[0] - curr_stop)
        else:
            rest_fuel = tank - (stops[0] - curr_stop)
            fuel_count += 1
        location += (stops[0] - curr_stop)
        curr_stop = stops[0]
        stops.pop(0)

    return fuel_count


def test_cases():
    if compute_min_refills(950, 400, [200, 375, 550, 750]) == 2:
        print('first case success')
    else:
        print('first case failed')

    if compute_min_refills(10, 3, [1, 2, 5, 9]) == -1:
        print('second case success')
    else:
        print('second case failed')


if __name__ == '__main__':
    # test_cases()
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
