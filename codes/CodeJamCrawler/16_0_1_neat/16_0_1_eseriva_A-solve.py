#!/usr/bin/pypy

import sys
infile = sys.argv[1]
try:
    outfile = sys.argv[2]
except IndexError:
    outfile = sys.stdout

def read_int(f):
    return int(f.readline())

def read_ints(f, sep=" "):
    return map(int, f.readline().rstrip().split(sep))

def read_lines(f, no_lines):
    retval = []
    for i in xrange(no_lines):
        retval.append(f.readline().rstrip())
    return retval

def solve(n):
    if n == 0:
        return "INSOMNIA"

    digits = set()

    i = 2
    curr = n
    while True:
#        print "curr", curr
        digits.update(str(curr))
        if len(digits) == 10:
            return curr

        curr = i * n
        i = i + 1
    
def main():
    f = open(infile, "r")
    no_cases = read_int(f)

    out = open(outfile, "w")
    
    for case_idx in xrange(no_cases):
        sol = solve(read_int(f))
        out.write("Case #%d: %s\n" % (case_idx+1, sol))
        

if __name__ == "__main__":
    main()
    
    