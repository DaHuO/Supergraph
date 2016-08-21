#!/usr/bin/env python

# Google Code Jam 2016
# Round 1B
# A. Getting the Digits
# patsp

digitStrings = ["ZERO", "ONE", "TWO", "THREE",
                "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
nDigits = 10
def go(dictSIn, ans):
    allNotAll = True
    done = True
    for n in range(nDigits):
        dictS = dictSIn.copy()
        all = True
        for ch in digitStrings[n]:
            if ch in dictS and dictS[ch] > 0:
                dictS[ch] -= 1
                done = False
            else:
                all = False
        if all:
            allNotAll = False
            (good, ansStr) = go(dictS.copy(), ans + str(n))
            if good:
                return (True, ansStr)
    if allNotAll and done:
        return (True, ans)
    return (False, '')

nTests = int(input())
for t in range(1, nTests + 1):
    s = input()
    dictS = {}
    for ch in s:
        if ch in dictS:
            dictS[ch] += 1
        else:
            dictS[ch] = 1
    (good, ans) = go(dictS, "")
    print('Case #{0}: {1}'.format(t, ans))
