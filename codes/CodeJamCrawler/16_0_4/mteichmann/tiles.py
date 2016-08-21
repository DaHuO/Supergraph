#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import itertools as it
import pickle
import logging
import math
import sys

reload(logging)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO,
                    stream=sys.stdout)


def tile_pos(tile, pos, K, C):
    return str(K*tile + pos + 1)


def solve(line):
    K, C, S = map(int, line.split(" "))
    output = ""
    for i in range(K):
        output += str(i+1) + " "
    return output



    num_checks = int(math.ceil(K/C))
    if S < num_checks:
        return "IMPOSSIBLE"
    logging.debug("K//C: %i" % (K//C))
    for i in range(K//C):
        pos = 0
        for j in range(C):
            pos += (i*C+j)*K**(C-j)
        output += str(pos+1) + " "
    pos = 0
    logging.debug("K mod C: %i" % (K % C))
    for j in range(K % C):
        pos += (K//C+j)*K**(C-j)
        logging.debug("j: %i pos: %i" % (j, pos))
    if K % C:
        output += str(pos+1) + " "

    return output

if __name__ == "__main__":
    lines = [line.rstrip() for line in open(sys.argv[1])]
    testcases = int(lines[0])

    for caseNr in range(1, testcases+1):
        print("Case #%i: %s" % (caseNr, solve(lines[caseNr])))
