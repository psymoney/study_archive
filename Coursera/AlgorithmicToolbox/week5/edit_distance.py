"""
## Edit Distance

# Problem Introduction

The edit distance between two strings is the minimum number of operations (insertions, deletions, and
substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.
Edit distance has applications, for example, in computational biology, natural language processing, and spell
checking. Your goal in this problem is to compute the edit distance between two strings.

# Problem Description
Task.           The goal of this problem is to implement the algorithm for computing the edit distance between two trings.
Input Format.   Each of the two lines of the input contains a string consisting of lower case latin letters.
Constraints.    The length of both strings is at least 1 and at most 100.
Output Format.  Output the edit distance between the given two strings.
"""
DEBUG = False


def edit_distance(s, t):
    distance = [[0] * len(t) for i in range(len(s))]
    for i in range(len(s)):
        distance[i][0] = i

    for j in range(len(t)):
        distance[0][j] = j

    for j in range(len(t)):
        for i in range(len(s)):
            insertion = distance[i][j-1] + 1
            deletion = distance[i-1][j] + 1
            match = distance[i-1][j-1]
            mismatch = distance[i-1][j-1] + 1

            if s[i] == t[j]:
                distance[i][j] = min(insertion, deletion, match)
            else:
                distance[i][j] = min(insertion,deletion,mismatch)

    if DEBUG:
        for i in range(len(s)):
            print(distance[i])

    return distance[-1][-1]


def test_case():
    if edit_distance('ab', 'ab') == 0:
        print('first test passed')
    else:
        print('first test failed')

    if edit_distance('short', 'posts') == 3:
        print('second test passed')
    else:
        print('second test failed')

    if edit_distance('EDITING', 'DISTANCE') == 5:
        print('third test passed')
    else:
        print('third test failed')


if __name__ == "__main__":
    if DEBUG:
       test_case()
    print(edit_distance(input(), input()))
