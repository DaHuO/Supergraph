#!/usr/bin/env python3

import sys

def sleep(x):
    if x == 0:
        return "INSOMNIA"
    else:
        s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        su = x
        while True:
            string = str(su)
            for c in string:
                if c in s:
                    s.remove(c)
                    if len(s) == 0:
                        return str(su)
            su += x



n = []
for line in sys.stdin:
    n.append(int(line))

for i in range(1, len(n)):
    print("Case #%d: %s" % (i, sleep(n[i])))
