#! /usr/bin/env python3

"""
https://code.google.com/codejam/contest/dashboard?c=6254486#s=p0
"""

def count_sheep(s):
    if s == '0':
        return "INSOMNIA"
    else:
        seen = set()
        for d in s:
            seen.add(d)

        multiplier = 1
        si = int(s)

        while len(seen) != 10:
            multiplier += 1
            cs = si * multiplier
            ss = str(cs)

            for c in ss:
                seen.add(c)

        return si * multiplier

if __name__ == "__main__":
    casecount = int(input())
    
    for i in range(casecount):
        print("Case #%d: %s" % ((i + 1), count_sheep(input())))
