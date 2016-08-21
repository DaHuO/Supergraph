#!/usr/local/bin/python3
import numpy as np
c = int(input())


ALPHA = "".join([chr(ord("A") + i) for i in range(0, 26)])


def solve():
    """A"""
    r = []
    n = int(input())
    data = [int(elem) for elem in input().split()]
    total = sum(data)
    while total > 0:
        idx0 = np.argmax(data)
        data[idx0] -= 1
        total -= 1
        if np.sum([total - data[i] < data[i] for i in range(n)]) > 0:
            idx1 = np.argmax(data)
            data[idx1] -= 1
            total -= 1
            r.append(ALPHA[idx0] + ALPHA[idx1])
        else:
            r.append(ALPHA[idx0])

    return " ".join(r)

for case in range(c):
    print('Case #{}: {}'.format(case + 1, solve()))
