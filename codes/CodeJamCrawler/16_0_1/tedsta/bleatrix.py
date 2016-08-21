#!/usr/bin/env python3

import sys

def count_digits(n):
    if n == 0:
        return "INSOMNIA"
    else:
        digits_seen = set(str(n))
        last = n
        while len(digits_seen) < 10:
            last += n
            digits_seen.update(str(last))
        return str(last)
    

def main():
    if len(sys.argv) < 2:
        print("Usage: bleatrix.py <file>")
    in_file = sys.argv[1]
    with open(in_file) as f:
        cases = int(f.readline())
        for i, line in enumerate(f):
            print("Case #%d: %s" % (i+1, count_digits(int(line))))

##########

if __name__ == '__main__':
    main()
