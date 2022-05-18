"""
## Maximum Salary

# Problem Introduction
As the last question of a successful interview, your boss gives you a few pieces of paper
with numbers on it and asks you to compose a largest number from these numbers. The
resulting number is going to be your salary, so you are very much interested in maximizing
this number. How can you do this?

    In the lectures, we considered the following algorithm for composing the largest number out of the given
    single-digit numbers.

LargestNumber(Digits):
    answer ← empty string
    while Digits is not empty:
        maxDigit ← −∞
        for digit in Digits:
            if digit ≥ maxDigit:
                maxDigit ← digit
        append maxDigit to answer
        remove maxDigit from Digits
    return answer

Unfortunately, this algorithm works only in case the input consists of single-digit numbers. For example, for
an input consisting of two integers 23 and 3 (23 is not a single-digit number!) it returns 233, while the largest
number is in fact 323. In other words, using the largest number from the input as the first number is not a
safe move.
Your goal in this problem is to tweak the above algorithm so that it works not only for single-digit
numbers, but for arbitrary positive integers.

# Problem Description
Task.           Compose the largest number out of a set of integers.
Input Format.   The first line of the input contains an integer 𝑛. The second line contains integers 𝑎1, 𝑎2, . . . , 𝑎𝑛.
Constraints.    1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑎𝑖 ≤ 10^3 for all 1 ≤ 𝑖 ≤ 𝑛.
Output Format.  Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.
"""
import sys


def largest_number(digits):
    numbers_in_order = []
    while len(digits) > 0:
        max_digit = -1
        for digit in digits:
            if is_greater_or_equal(int(digit), max_digit):
                max_digit = int(digit)
        numbers_in_order.append(max_digit)
        digits.remove(max_digit)
    concatenated_numbers = ''
    for n in numbers_in_order:
        concatenated_numbers += str(n)
    return int(concatenated_numbers)


def get_first_digit(number):
    while number >= 10:
        number = number // 10
    return number


def is_greater_or_equal(a, b):
    if b == -1:
        return True
    a_b = str(a) + str(b)
    b_a = str(b) + str(a)
    a_b = int(a_b)
    b_a = int(b_a)

    if a_b >= b_a:
        return True
    else:
        return False

# def is_greater_or_equal(a, b):
#     if b == -1:
#         return True
#     a_list = []
#     b_list = []
#
#     while a >= 10:
#         a_list.insert(0, a % 10)
#         a = a // 10
#     a_list.insert(0, a)
#
#     while b >= 10:
#         b_list.insert(0, b % 10)
#         b = b // 10
#     b_list.insert(0, b)
#
#     while len(a_list) > 0 and len(b_list) > 0:
#         if a_list[0] == b_list[0]:
#             a_list.pop(0)
#             b_list.pop(0)
#             continue
#         elif a_list[0] > b_list[0]:
#             return True
#         elif a_list[0] < b_list[0]:
#             return False
#     if len(a_list) == 0:
#         return True
#     elif len(b_list) == 0:
#         return False


def test_cases():
    if largest_number([21, 2]) == 221:
        print('first test success')
    else:
        print('first test failed')
    if largest_number([9, 4, 6, 1, 9]) == 99641:
        print('second test success')
    else:
        print('second test failed')
    if largest_number([23, 39, 92]) == 923923:
        print('third test success')
    else:
        print('third test failed')
    if largest_number([2, 8, 2, 3, 6, 4, 1, 1, 10, 6, 3, 3, 6, 1, 3, 8, 4, 6, 1, 10, 8, 4, 10, 4, 1, 3, 2, 3,
                       2, 6, 1, 5, 2, 9, 8, 5, 10, 8, 7, 9, 6, 4, 2, 6, 3, 8, 8, 9, 8, 2, 9, 10, 3, 10, 7, 5,
                       7, 1, 7, 5, 1, 4, 7, 6, 1, 10, 5, 4, 8, 4, 2, 7, 8, 1, 1, 7, 4, 1, 1, 9, 8, 6, 5, 9, 9,
                       3, 7, 6, 3, 10, 8, 10, 7, 2, 5, 1, 1, 9, 9, 5]) == 9999999998888888888887777777776666666666555555554444444443333333333222222222111111111111111101010101010101010:
        print('fourth test success')
    else:
        print('fourth test failed')

    if largest_number([999, 987, 1, 10, 9, 19, 91, 109, 901]) == 99999879190119110910:
        print('fifth test success')
    else:
        print('fifth test failed')


if __name__ == '__main__':
    # test_cases()
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    for i in range(len(a)):
        a[i] = int(a[i])
    print(largest_number(a))
    
