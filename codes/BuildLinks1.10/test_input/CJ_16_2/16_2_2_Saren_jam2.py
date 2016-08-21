#!/usr/bin/env python3
from itertools import product
FORMAT = "Case #{}: {} {}"

if __name__ == "__main__":
    cases = int(input())
    for t in range(cases):
        i, j = input().split()
        qci, qcj = i.count("?"), j.count("?")
        qc = qci + qcj
        if qc == 0:
            print(FORMAT.format(t + 1, i, j))
            continue
        d = {}
        stop = False
        for p in product(range(10), repeat=qc):
            p_i = 0
            tmp_i = i
            tmp_j = j
            for q in range(qci):
                tmp_i = tmp_i.replace("?", str(p[p_i]), 1)
                p_i += 1
            for q in range(qcj):
                tmp_j = tmp_j.replace("?", str(p[p_i]), 1)
                p_i += 1
            int_i, int_j = int(tmp_i), int(tmp_j)
            diff = abs(int_i - int_j)
            if diff == 0:
                print(FORMAT.format(t + 1, tmp_i, tmp_j))
                stop = True
                break
            d[(tmp_i, tmp_j)] = diff
        if stop:
            continue
        min_diff = d[min(d, key=d.get)]
        candidates = []
        for k, v in d.items():
            if v == min_diff:
                candidates.append(k)
        best = min(candidates, key=lambda x: int(x[0]) + int(x[1]))
        print(FORMAT.format(t + 1, best[0], best[1]))
