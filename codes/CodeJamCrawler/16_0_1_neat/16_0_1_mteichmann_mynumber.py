#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import itertools as it
import pickle
import logging
import sys

reload(logging)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO,
                    stream=sys.stdout)


def solve(i):
    i = int(i)
    if i == 0:
        return "INSOMNIA"
    a = np.zeros(10) != np.zeros(10)

    logging.debug("Process Numer: %i", i)
    mult = 0
    while not np.all(a):
        mult = mult+1
        logging.debug("Arriving at: %i (Multiplication: %i " % (mult*i, i))
        for dig in map(int, str(mult*i)):
            a[dig] = True
        logging.debug("Found Numbers: %s", a)
    return mult*i

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
