#!/usr/bin/env python
import itertools
import sys

def find_repeat(num):
    if num == 0: return "INSOMNIA"
    curr = 0
    digits = set()
    for i in itertools.count(1):
        curr += num
        digits.update(set(str(curr)))
        if len(digits) == 10:
            return curr

def main(argv=sys.argv):
    infile = argv[1]
    outfile = argv[2]
    cases = []
    with open(infile) as f:
        num_cases = int(f.readline())
        for _ in xrange(num_cases):
            cases.append(int(f.readline()))

    with open(outfile, 'w') as g:
        for i, c in enumerate(cases, 1):
            g.write("Case #{}: {}\n".format(i, find_repeat(c)))
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
