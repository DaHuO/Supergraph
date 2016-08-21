#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys

with open(sys.argv[1], 'r') as f:
    for k in range(int(f.readline())):
        S = f.readline().strip()
        res = [S[0]]
        for letter in S[1:]:
            if letter >= res[0]:
                res.insert(0, letter)
            else:
                res.append(letter)
        print("Case #"+str(k+1)+": "+''.join(res))
