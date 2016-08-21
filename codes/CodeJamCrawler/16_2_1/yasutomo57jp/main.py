#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import sys

T = int(sys.stdin.readline().strip())

nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

chars = {"E":0, "F":1, "G":2, "H":3, "I":4, "N":5, "O":6, "R":7, "S":8, "T":9, "U":10, "V":11, "W":12, "X":13, "Z":14}



hists = {}
for n in range(len(nums)):
    h = [0] * len(chars)
    for c in nums[n]:
        h[chars[c]] += 1
    hists[n] = h

maps = {}
for i in range(len(chars)):
    maps[i] = [0]*10

for i, h in hists.items():
    for j, v in enumerate(h):
        maps[j][i] = v


def check(S):
    resulthist = [0] * 10
    sumhist = np.asarray([0] * len(chars), dtype=np.int)
    for c in S:
        sumhist[chars[c]] += 1

    resulthist[0] = sumhist[chars["Z"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[0], dtype=np.int) * resulthist[0]

    resulthist[6] = sumhist[chars["X"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[6], dtype=np.int) * resulthist[6]

    resulthist[2] = sumhist[chars["W"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[2], dtype=np.int) * resulthist[2]

    resulthist[4] = sumhist[chars["U"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[4], dtype=np.int) * resulthist[4]

    resulthist[8] = sumhist[chars["G"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[8], dtype=np.int) * resulthist[8]

    resulthist[1] = sumhist[chars["O"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[1], dtype=np.int) * resulthist[1]

    resulthist[3] = sumhist[chars["T"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[3], dtype=np.int) * resulthist[3]

    resulthist[5] = sumhist[chars["F"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[5], dtype=np.int) * resulthist[5]

    resulthist[7] = sumhist[chars["S"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[7], dtype=np.int) * resulthist[7]

    resulthist[9] = sumhist[chars["E"]]
    # print(sumhist)
    sumhist -= np.asarray(hists[9], dtype=np.int) * resulthist[9]

    # print(sumhist, resulthist)

    result = ""
    for i, s in enumerate(resulthist):
        # print(i, s)
        result += str(i) * s

    return result

case = 1
while True:
    s = sys.stdin.readline().strip()
    if s == "":
        break
    result = check(s)

    print("Case #%d: %s" % (case, result))

    case += 1
