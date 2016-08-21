#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

with open(argv[1]) as f:
    case = 1
    f.readline();
    for line in f:
        line = line.strip()
        flips = 0
        last = '+'
        for c in line:
            if last != c:
                flips = flips + 1
            last = c

        if last == '+':
            flips = max(0, flips - 1)
        if line[0] == '+' and flips != 0:
            flips = flips + 1
        print "Case #" + str(case) + ": " + str(flips)
        case = case + 1
