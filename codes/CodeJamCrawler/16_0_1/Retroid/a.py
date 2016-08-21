#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

with open(argv[1]) as f:
    case = 0
    for line in f:
        n = int(line)
        nCopy = n
        found = set()
        count = 1
        while len(found) != 10 and nCopy != 0:
            string = str(nCopy)
            for c in string:
                found.add(c)
            count += 1
            nCopy = n*count
        if nCopy == 0:
            print "Case #" + str(case) + ": INSOMNIA"
        else:
            print "Case #" + str(case) + ": " + str(n * (count-1))
        case = case + 1
