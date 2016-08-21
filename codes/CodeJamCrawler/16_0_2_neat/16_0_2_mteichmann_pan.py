#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import itertools as it
import pickle
import logging
import sys

reload(logging)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


def solve(line):
    if line[-1] == '-':
        num_op = 1
    elif line[-1] == '+':
        num_op = 0
    else:
        assert(False)

    for i in range(len(line)-1):
        if line[i] != line[i+1]:
            num_op += 1

    return num_op

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
