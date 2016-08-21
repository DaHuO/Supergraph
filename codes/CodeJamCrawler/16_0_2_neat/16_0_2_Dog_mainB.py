#! /usr/bin/env python3
import re
import sys

def solve(case):
    case = re.sub(r'([+]+)', '+', case)
    case = re.sub(r'([-]+)', '-', case)
    return len(case) - {'+':1, '-':0}[case[-1]]

with open(sys.argv[1]) as f:
    content = f.read().strip()

cases = content.split('\n')[1:]
for (c, n) in enumerate(cases, 1):
    print("Case #{}:".format(c), solve(n))
