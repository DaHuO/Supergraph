#!/usr/bin/env python

__author__ = 'Bill'

def check_pancakes(n):
    """(check_pancakes):
        function to test for all face up
        :param n: the pancakes string
    """
    for ch in n:
        if ch == '-':
            return False
    return True


def flip_pancakes(n):
    """(flip_pancakes):
        function to flip pancakes
        :param n: the pancakes string
    """
    n = list(n)
    dict = {'+':'-', '-':'+'}
    first = n[0]
    i = 0
    for ch in n:
        if ch != first:
            break
        i += 1
    for j in xrange(i):
        n[j] = dict[first]
    n = "".join(n)
    return n


from misc import input_, output_

num_cases, cases = input_('B-large.in')

Results = []

for case in cases:
    case = case.rstrip('\n')
    i = 0
    face_up = check_pancakes(case)
    if face_up == True:
        Results.append(i)
    else:
        while check_pancakes(case) == False:
            case = flip_pancakes(case)
            i += 1
        Results.append(i)

output_(Results, 'Revenge_of_the_pancakes_large.out')