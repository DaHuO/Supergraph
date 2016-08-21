#!/usr/bin/env python
import sys
import re
def find_optimal_scores(C, J):
    digits_cnt = len(C)
    numbers = ["{:03d}".format(num)[-digits_cnt:] for num in range(10**digits_cnt)]
    c_re = re.compile(C.replace("?", "."))
    j_re = re.compile(J.replace("?", "."))
    c_options = [num for num in numbers if c_re.match(num)]
    j_options = [num for num in numbers if j_re.match(num)]
    min_diff = 1000
    min_c = ""
    min_j = ""
    for c in c_options:
        for j in j_options:
            diff = abs(int(c) - int(j))
            if diff < min_diff:
                min_c = c
                min_j = j
                min_diff = diff
    return min_c, min_j

lines = [l.strip() for l in sys.stdin.readlines()]
T = int(lines[0])
assert(T == len(lines)-1)
for i in range(1, T+1):
    C, J = lines[i].strip().split()
    assert(len(C) == len(J))
    assert(len(C) <= 3 and len(C) >= 1)
    sys.stderr.write("Processing case #{}\n".format(i))
    c, j = find_optimal_scores(C, J)
    sys.stdout.write("Case #{}: {} {}\n".format(i, c, j))
