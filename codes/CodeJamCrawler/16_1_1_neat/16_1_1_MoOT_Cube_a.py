#!/usr/bin/env python

import sys


if __name__ == "__main__":
    for (k, i) in enumerate([l.rstrip("\n") for l in sys.stdin.readlines()[1:]]):
        l = list(i)
        s = list(l[0])
        for j in l[1:]:
            if j >= s[0]:
                s.insert(0, j)
            else:
                s.append(j)
        print("Case #" + str(k + 1) + ": " + "".join(s))
