#!/usr/bin/python3

# pycosat can be found here
# https://pypi.python.org/pypi/pycosat
import pycosat

# 0-49 : unknown is row i
# 50-99 : unknown is col i-50
# 100 + ... : line i is row j / column j

def id_line_row(i, j):
    return 1 + 100 + 100 * i + j

def id_line_col(i, j):
    return 1 + 100 + 100 * i + 50 + j

def run():
    n = int(input().strip())
    lines = list([int(x) for x in input().split()] for _ in range(2 * n - 1))
    cdt = []
    for i in range(n):
        cdt.append([ 1 + i] + [id_line_row(j, i) for j in range(2*n - 1)])
        cdt.append([51 + i] + [id_line_col(j, i) for j in range(2*n - 1)])

    for i in range(n):
        for j in range(n):
            cdt.append([-1 - i, -51 - j])
            if i <= j:
                continue
            cdt.append([-1 - i, -1 - j])
            cdt.append([-51 - i, -51 - j])
        for k in range(len(lines)):
            for j in range(n):
                cdt.append([-id_line_row(k, i), -id_line_col(k, j)])
                if i <= j:
                    continue
                cdt.append([-id_line_row(k, i), -id_line_row(k, j)])
                cdt.append([-id_line_col(k, i), -id_line_col(k, j)])

    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j:
                continue
            for r in range(n):
                for c in range(n):
                    if lines[i][c] != lines[j][r]:
                        cdt.append([-id_line_row(i, r), -id_line_col(j, c)])

    # print(cdt)

    sol = pycosat.solve(cdt)

    res = None
    m = list(n * [None] for _ in range(n))
    for i in sol:
        if i < 0:
            continue
        # print(i)
        i -= 1
        if i < 100:
            res = i
            continue
        i -= 100
        l = i // 100
        j = i % 100
        if j < 50:
            # print("(%d) %s is the %d-th row" % (l, " ".join("%d" % x for x in lines[l]), j))
            for k in range(n):
                m[j][k] = lines[l][k]
        else:
            j -= 50
            # print("(%d) %s is the %d-th col" % (l, " ".join("%d" % x for x in lines[l]), j))
            for k in range(n):
                m[k][j] = lines[l][k]

    if res < 50:
        return " ".join("%d" % m[res][k] for k in range(n))
    else:
        res -= 50
        return " ".join("%d" % m[k][res] for k in range(n))

    

t = int(input().strip())
for i in range(t):
    print("Case #%d: %s" % (i+1, run()))
