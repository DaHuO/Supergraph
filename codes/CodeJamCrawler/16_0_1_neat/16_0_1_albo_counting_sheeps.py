#!/usr/bin/python

import sys, os
import readline

test_cases = None
test_case = None

def test_number(n):
    s = "%i" % n

    if s == "0":
        return "INSOMNIA"

    last = ""
    d = {}
    run = 0
    while len(d.keys()) < 10:
        run += 1
        s = "%i" % (run*n)

        for i in s:
            d[i] = True

    return s 

if __name__ == "__main__":
    f = open(sys.argv[1], "r")

    while True:
        line = f.readline()
        if line == None or len(line) == 0:
            break

        try:
            val = int(line)
        except ValueError:
            break

        if test_cases == None:
            test_cases = val
            test_case = 0
            continue
        else:
            test_case += 1

        if test_case <= test_cases:
            print("Case #%i: %s" % (test_case, test_number(val)))
        else:
            break

    f.close()
        
    sys.exit(0)
