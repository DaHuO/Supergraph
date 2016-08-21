import sys

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

## ALGORITHM ==================================================================

def problem(data):
    ll = data; ww = 0
    dd = range(0, 10); aa = 2

    while 1:
        xx = len(dd)
        for a in str(data):
            if int(a) in dd: dd.remove(int(a))
        if len(dd) == 0:
            break
        if len(dd) == xx:
            ww += 1
        if ww == len(str(ll)) * 1000:
            break
        data = int(ll) * int(aa); aa += 1

    if len(dd) != 0:
        return "INSOMNIA"
    else:
        return data

## INTERFACE ==================================================================

data = sys.stdin.read().strip().split('\n'); data.pop(0)

for line in range(0, len(data)):
    result = problem(data[line])
    print("Case #{0}: {1}".format(line + 1, result))
