#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    pattern = re.compile(r'^(\d+) (\d+) (\d+)$')
    for case_id in xrange(1, T + 1):
        line = sys.stdin.readline()[:-1]
        match = pattern.match(line)
        K, C, S = int(match.group(1)), int(match.group(2)), int(match.group(3))

        base = K ** (C - 1)
        tiles = []
        for index in xrange(S):
            tiles.append(1 + index * base)

        print "Case #%d: %s" % (case_id, ' '.join([str(i) for i in tiles]))
