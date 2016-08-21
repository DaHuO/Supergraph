#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i, case in enumerate(range(int(input().strip())), 1):
    letters = list(input().strip())
    temp = letters[0]
    mlist = [temp]

    for l in letters[1:]:
        if l < temp:
            mlist.append(l)
        else:
            mlist.insert(0, l)
            temp = l

    print("Case #{0:s}:".format(str(i)), ''.join(mlist))
