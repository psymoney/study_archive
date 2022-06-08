"""
## Maximum Value of an Arithmetic Expression

# Problem Introduction
    In this problem, your goal is to add parentheses to a given arithmetic
    expression to maximize its value. max(5−8+7×4−8+9) =?

# Problem Description
    Task.           Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic
                    operations using additional parentheses.
    Input Format.   The only line of the input contains a string 𝑠 of length 2𝑛 + 1 for some 𝑛, with symbols
                    𝑠0, 𝑠1, . . . , 𝑠2𝑛. Each symbol at an even position of 𝑠 is a digit (that is, an integer from 0 to 9) while
                    each symbol at an odd position is one of three operations from {+,-,*}.
    Constraints.    0 ≤ 𝑛 ≤ 14 (hence the string contains at most 29 symbols).
    Output Format.  Output the maximum possible value of the given arithmetic expression among different
                    orders of applying arithmetic operations.

# Sample 1.
    Input:
        1+5
    Output:
        6

# Sample 2.
    Input:
        5-8+7*4-8+9
    Output:
        200
        200 = (5 − ((8 + 7) × (4 − (8 + 9))))

"""
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    return 0


if __name__ == "__main__":
    print(get_maximum_value(input()))
