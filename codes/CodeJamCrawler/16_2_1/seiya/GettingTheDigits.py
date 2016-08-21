#!/usr/bin/env python
# -*- coding: utf-8 -*-

inFile = open("input.txt","r")
outFile = open("output.txt","w")


def delStr(s, strlist):
    for i in range(len(strlist)):
        idx = s.find(strlist[i])
        s = s[:idx] + s[idx+1:]
    return s

def solve(case, S):


    results = []
    lastCount = 0

    # check1
    # 0 ZERO: Z
    # 1 ONE
    # 2 TWO: W
    # 3 THREE:
    # 4 FOUR:
    # 5 FIVE:
    # 6 SIX: X
    # 7 SEVEN:
    # 8 EIGHT: G
    # 9 NINE:
    while True:
        if S.find("Z") >= 0:
            results.append(0)
            S = delStr(S, "ZERO")
        if S.find("W") >= 0:
            results.append(2)
            S = delStr(S, "TWO")
        if S.find("X") >= 0:
            results.append(6)
            S = delStr(S, "SIX")
        if S.find("G") >= 0:
            results.append(8)
            S = delStr(S, "EIGHT")
        if len(results) == lastCount:
            break
        else:
            lastCount = len(results)

    # check2
    # 1 ONE
    # 3 THREE: T
    # 4 FOUR:
    # 5 FIVE:
    # 7 SEVEN: S
    # 9 NINE:
    while True:
        if S.find("T") >= 0:
            results.append(3)
            S = delStr(S, "THREE")
        if S.find("S") >= 0:
            results.append(7)
            S = delStr(S, "SEVEN")
        if len(results) == lastCount:
            break
        else:
            lastCount = len(results)
    # check3
    # 1 ONE
    # 4 FOUR: R
    # 5 FIVE:
    # 9 NINE:
    while True:
        if S.find("R") >= 0:
            results.append(4)
            S = delStr(S, "FOUR")
        if len(results) == lastCount:
            break
        else:
            lastCount = len(results)
    # check4
    # 1 ONE: O
    # 5 FIVE: F
    # 9 NINE:
    while True:
        if S.find("O") >= 0:
            results.append(1)
            S = delStr(S, "ONE")
        if S.find("F") >= 0:
            results.append(5)
            S = delStr(S, "FIVE")
        if len(results) == lastCount:
            break
        else:
            lastCount = len(results)
    # check5
    # 9 NINE:
    while True:
        if S.find("N") >= 0:
            results.append(9)
            S = delStr(S, "NINE")
        if len(results) == lastCount:
            break
        else:
            lastCount = len(results)
    results.sort()
    resstr = ""
    for i in range(len(results)):
        resstr += "%d" % results[i]

    return "Case #%d: %s\n" % (case, resstr)

if __name__ == "__main__":
    isFirst = True
    totalCase = 0
    currentCase = 1

    for line in inFile.readlines():
        items = line.split()

        # first Line
        if isFirst == True:
            isFirst = False
            totalCase = int(items[0])
            continue

        # execute
        out = solve(currentCase, items[0])
        outFile.write(out)
        print out

        # go next
        currentCase = currentCase + 1
        if currentCase > totalCase:
            break
