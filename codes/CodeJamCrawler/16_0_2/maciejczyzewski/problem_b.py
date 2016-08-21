import sys

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

## ALGORITHM ==================================================================

def problem(data):
    stack = data.replace('-', '1').replace('+', '0')
    if int(stack, 2) == 0: return 0 # happy?
    if '0' not in stack: return 1 # very sad?

    stack = list(stack); w = 0; v = 0

    while 1:
        if stack[0] == '1': b = '1'; c = '0'
        if stack[0] == '0': b = '0'; c = '1'

        for char in stack:
            if char == b:
                stack[w] = c; w += 1
            else:
                v += 1; w = 0; break

        if '0' not in stack or '1' not in stack:
            break

    if '0' not in stack: v += 1

    return v

## INTERFACE ==================================================================

data = sys.stdin.read().strip().split('\n'); data.pop(0)

for line in range(0, len(data)):
    result = problem(data[line])
    print("Case #{0}: {1}".format(line + 1, result))
