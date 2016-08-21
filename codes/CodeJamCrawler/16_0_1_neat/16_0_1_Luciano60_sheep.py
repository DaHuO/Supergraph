def solve(inp):
    if (int(inp) == 0):
        return "INSOMNIA"
    else:
        s = set()
        i = 1
        nb = int(inp)
        while (len(s) != 10):
            nb = int(inp) * i
            for d in str(nb):
                s.add(d)
            i += 1
        return str(nb)
        

#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
