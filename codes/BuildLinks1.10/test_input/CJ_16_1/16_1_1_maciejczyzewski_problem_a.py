import sys

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

## ALGORITHM ==================================================================

def problem(data):
    letters = list(data); final = ''
    for char in letters:
        if final == '':
            final = char; continue
        if final[0] <= char:
            final = char + final
        else:
            final = final + char
    return final

## INTERFACE ==================================================================

data = sys.stdin.read().strip().split('\n'); data.pop(0)

for line in range(0, len(data)):
    result = problem(data[line])
    print("Case #{0}: {1}".format(line + 1, result))
