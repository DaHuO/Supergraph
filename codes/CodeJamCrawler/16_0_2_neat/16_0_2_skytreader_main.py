#! /usr/bin/env python3

"""
https://code.google.com/codejam/contest/dashboard?c=6254486#s=p1
"""

def count_transitions(s):
    """
    Assumes that the string s is just + or - signs.
    """
    count = 0
    curchar = s[0]

    for c in s[1:]:
        if c != curchar:
            count += 1
            curchar = c

    return count if s[-1] == '+' else (count + 1)

if __name__ == "__main__":
    casecount = int(input())
    
    for i in range(casecount):
        print("Case #%d: %d" % ((i + 1), count_transitions(input())))
