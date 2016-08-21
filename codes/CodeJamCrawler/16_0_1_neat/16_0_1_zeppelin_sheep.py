import numpy as np
from collections import Counter
from math import *


f = file('input.txt')
out = open('output.txt', 'w+')
T = int(f.readline())
for t in range(1, T + 1):
    N = int(f.readline())
    digits = set()
    i = 1
    n = N
    if N != 0:
        while True:
            n = N*i
            digits = digits.union(set(str(n)))
            if len(digits) == 10:
                break
            i += 1
    else:
        n = "INSOMNIA"
    line = "Case #" + str(t) + ": " + str(n)
    print(line)
    out.write(line + "\n")
f.close()
out.close()
