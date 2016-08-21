#!/usr/bin/env python

import sys
import os
import math
from collections import defaultdict, Counter
from itertools import izip

DEBUG = False

def make_answer(ngrid, col_lines):
    empty_line = None
    j = 0
    for i in xrange(len(ngrid)):
        if j == len(col_lines) or ngrid[i] != col_lines[j]:
            if empty_line is None:
                empty_line = ngrid[j]
            else:
                return None
        else:
            j += 1
    return empty_line


def check_answer(middle_lines, col_lines, left, right, grid, rownum):
    if DEBUG: print((len(middle_lines), len(col_lines), len(grid), rownum))
    if DEBUG: print(middle_lines, col_lines, left, right, grid, rownum)
    if rownum == len(grid):
        ngrid = list(izip(*grid))
        if left is None:
            return make_answer(ngrid, col_lines+[right])
        elif right is None:
            return make_answer(ngrid, [left]+col_lines)
        else:
            return make_answer(ngrid, [left]+col_lines+[right])

    if left is None:
        x1 = None
    else:
        x1 = left[rownum]
    if right is None:
        x2 = None
    else:
        x2 = right[rownum]

    if x1 is not None:
        for i in xrange(len(middle_lines)):
            midline = middle_lines[i]
            if DEBUG: print(midline)
            if midline[0] != x1:
                #col_lines.append(midline)
                continue
                #
                #elif midline[0] > x1:
                #    if DEBUG: print("CHECK1")
                #    return None
            elif midline[0] == x1 and x2 is not None and midline[-1] != x2:
                #col_lines.append(midline)
                continue
            else:
                grid[rownum] = midline
                ans = check_answer(middle_lines[i+1:], col_lines+middle_lines[:i], left, right, grid, rownum+1)
                if ans is None:
                    #col_lines.append(midline)
                    continue
                else:
                    return ans
        if DEBUG: print("CHECK2")
        return None
    else:
        for i in xrange(len(middle_lines)):
            midline = middle_lines[i]
            if DEBUG: print(midline)
            if midline[-1] != x2:
                #col_lines.append(midline)
                continue
            else:
                grid[rownum] = midline
                ans = check_answer(middle_lines[i+1:], col_lines+middle_lines[:i], left, right, grid, rownum+1)
                if ans is None:
                    #col_lines.append(midline)
                    continue
                else:
                    return ans
        if DEBUG: print("CHECK3")
        return None
            
"""        


    if rownum == len(left) - 1:
        pass
    x = left[rownum]
    for y in middle_lines[x]:
        grid[rownum] = y
        ans = check_answer(middle_lines, left, right, grid, rownum+1)
        if ans is not None: return ans
    grid[rownum] = None
    ans = check_answer_skip(middle_lines, left, right, grid, rownum+1, rownum)
    return ans

def check_answer(middle_lines, left, right, grid, rownum):
    if rownum == len(left) - 1:
        pass
    x = left[rownum]
    for y in middle_lines[x]:
        grid[rownum] = y
        ans = check_answer(middle_lines, left, right, grid, rownum+1)
        if ans is not None: return ans
    grid[rownum] = None
    ans = check_answer_skip(middle_lines, left, right, grid, rownum+1, rownum)
    return ans
    
        
def check_answer_skip(middle_lines, left, right, grid, rownum, skipnum):
    if rownum == len(left) - 1:
        pass
    x = left[rownum]
    for y in middle_lines[x]:
        grid[rownum] = y
        ans = check_answer_skip(middle_lines, left, right, grid, rownum+1, skipnum)
        if ans is not None: return ans
    return None
"""

def get_answer(f):
    N = int(f.readline().strip())
    alllines = []
    heights = set()
    for i in xrange(2*N - 1):
        line = map(int, f.readline().strip().split())
        alllines.append(tuple(line))
        heights.update(line)
    if DEBUG: print("Start "+str(N)+" "+str(alllines))
    topcorner = min(heights)
    bottomcorner = max(heights)
    topcorner_lines = []
    bottomcorner_lines = []
    middle_lines = []
    for line in alllines:
        if line[0] == topcorner:
            topcorner_lines.append(line)
        elif line[-1] == bottomcorner:
            bottomcorner_lines.append(line)
        else:
            middle_lines.append(line)
    middle_lines = sorted(middle_lines)
            
    if len(topcorner_lines) == 1:
        if DEBUG: print("CASE")
        ans = check_answer([topcorner_lines[0]] + middle_lines + [bottomcorner_lines[0]], [], None, bottomcorner_lines[1], [None]*N, 0) 
        if ans is None:
            ans = check_answer([topcorner_lines[0]] + middle_lines + [bottomcorner_lines[1]], [], None, bottomcorner_lines[0], [None]*N, 0)
    elif len(bottomcorner_lines) == 1:
        if DEBUG: print("CASE2")
        ans = check_answer([topcorner_lines[0]] + middle_lines + [bottomcorner_lines[0]], [], topcorner_lines[1], None, [None]*N, 0) 
        if ans is None:
            ans = check_answer([topcorner_lines[1]] + middle_lines + [bottomcorner_lines[0]], [], topcorner_lines[0], None, [None]*N, 0)
    else:
        if DEBUG: print("CASE3")
        ans = check_answer([topcorner_lines[0]] + middle_lines + [bottomcorner_lines[0]], [], topcorner_lines[1], bottomcorner_lines[1], [None]*N, 0) 
        if ans is None:
            ans = check_answer([topcorner_lines[1]] + middle_lines + [bottomcorner_lines[0]], [], topcorner_lines[0], bottomcorner_lines[1], [None]*N, 0)
        if ans is None:
            ans = check_answer([topcorner_lines[1]] + middle_lines + [bottomcorner_lines[1]], [], topcorner_lines[0], bottomcorner_lines[0], [None]*N, 0)
        if ans is None:
            ans = check_answer([topcorner_lines[0]] + middle_lines + [bottomcorner_lines[1]], [], topcorner_lines[1], bottomcorner_lines[0], [None]*N, 0)
    if ans is None:
        raise Exception("Answer is None!")
    return " ".join(map(str, ans))


if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = input_filename[:-3]+".out"
    if input_filename == "test":
        output_filename = "test.out"

    with open(input_filename) as f:
        with open(output_filename, "w") as g:
            T = int(f.readline().strip())
            for test_idx in xrange(1,T+1):
                if test_idx == -1: DEBUG = True
                ans = get_answer(f)
                g.write("Case #"+str(test_idx)+": "+str(ans)+"\n")

    #
