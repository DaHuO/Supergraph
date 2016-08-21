test_input = \
"""4
4
2 3 4 1
4
3 3 4 1
4
3 3 4 3
10
7 8 10 10 9 2 9 6 3 3"""
test_output = \
"""Case #1: 4
Case #2: 3
Case #3: 3
Case #4: 6"""

import itertools
import math
import sys
test = False
line_number = 0


def get_input():
    global line_number
    if not test:
        return raw_input("")
    else:
        output = test_input.split("\n")[line_number]
        line_number += 1
        return output

def valid_circle(circle, kids):
    # for every single kid, check to see if their friend is to their left or right
    # if not, return false
    length = len(circle)
    for i in range(length):
        if kids[circle[i]] != circle[i-1]:
            if kids[circle[i]] != circle[(i+1) % length]:
                return False
    return True


if __name__ == "__main__":
    cases = int(get_input())
    for case in range(cases):
        num_kids = int(get_input())
        # now grab the bffs for each kid
        kids = {}
        kids_str = get_input().split(" ")
        for i in range(num_kids):
            kids[i + 1] = int(kids_str[i])
        max_circle = num_kids
        valid_permutation = None

        # now we iterate across the possiblilities, decreasing it by 1 each time
        # if we ever find a valid circle we return that value
        # super brute force, can be optimized dramatically
        for size in range(max_circle, 1, -1):
            valid_permutation = None
            for permutation in itertools.permutations(range(1, num_kids+1), size):
                if valid_circle(permutation, kids):
                    valid_permutation = size
                    break
            if valid_permutation:
                break
        if valid_permutation:
            print "Case #{}: {}".format(case + 1, valid_permutation)
        else:
            print "Case #{}: 0".format(case + 1)


