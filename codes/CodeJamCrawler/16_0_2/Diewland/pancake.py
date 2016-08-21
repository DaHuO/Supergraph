#!/usr/bin/python

##########################################################

import re

def all_happy(pancakes):
    return pancakes.find('-') == -1

def flip(pancakes):
    return ''.join([ '+' if v == '-' else '-' for v in pancakes[::-1] ])

def can_flip_all(pancakes):
    return False

def find_flip_idx(pancakes, x='-'):
    y = '+' if x == '-' else '-'

    # find position to flip
    flip_idx = 0
    found_blank = False
    for idx, val in enumerate(pancakes):
        if val == x:
            flip_idx = idx
            found_blank = True
        elif found_blank and (val == y):
            flip_idx = idx-1
            break
    return flip_idx

def do_flip(pancakes):
    # get flip index
    flip_sign = pancakes[0]
    flip_idx = find_flip_idx(pancakes, flip_sign)

    # split to first and last
    first = pancakes[0: flip_idx+1]
    last  = pancakes[flip_idx+1:]
    #print "(%s)\t%s|%s" % ( flip_idx, first, last )

    # return
    return flip(first) + last

def process(pancakes, cnt=0):
    if all_happy(pancakes):
        return cnt
    else:
        cnt += 1
        return process(do_flip(pancakes), cnt)

##########################################################

import sys
total_cases = None
case_no = 1
with open(sys.argv[1]) as f:
    for line in f:
        if total_cases is None:
            total_cases = int(line)
        else:
            """
            if case_no != 85:
                case_no += 1
                continue # TODO
            print line
            """
            result = process(line.strip())
            print "Case #%s: %s" % ( case_no, result )
            case_no += 1
