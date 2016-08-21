#!/usr/bin/env python

import sys

tcase = 1
with open(sys.argv[1], 'r') as fin:
    n = -1
    for line in fin.readlines():
        line = line.strip()
        if n == -1:
            n = int(line)
        else:
            cnt = 0
            t = '-'
            while True:
                line = line[:line.rfind(t) + 1]
                if len(line) == 0:
                    break
                t = '+' if t == '-' else '-'
                cnt += 1

            print "Case #%d: %d" % (tcase, cnt)
            tcase += 1
