#!/usr/bin/python
import copy
import sys
sys.setrecursionlimit(1000000)

def check(word, arrs, count):
    warr = list(word)
    karrs = copy.copy(arrs)
    for c in warr:
        if c not in arrs:
            arrs[c] = 0
            karrs[c] = 0

        if karrs[c] == 0:
            return count
        karrs[c] = karrs[c] -1
    arrs = copy.copy(karrs)
    return check(word, arrs, count+1)


f = open('sample.txt', 'r')
tc = int(f.readline())
#print tc
for index in range(tc):
    result = ""
    strs = f.readline().rstrip()
    arr = list(strs)
    arrs = {}
    for c in arr:
        if c not in arrs:
            arrs[c] = 0
        arrs[c] += 1


    cnt = check("ZERO", arrs, 0)
    for k in range(cnt):
        result += "0"
        for c in list("ZERO"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1

    cnt = check("TWO", arrs, 0)
    for k in range(cnt):
        result += "2"
        for c in list("TWO"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1

    cnt = check("FOUR", arrs, 0)
    for k in range(cnt):
        result += "4"
        for c in list("FOUR"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1

    cnt = check("SIX", arrs, 0)
    for k in range(cnt):
        result += "6"
        for c in list("SIX"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1

    cnt = check("EIGHT", arrs, 0)
    for k in range(cnt):
        result += "8"
        for c in list("EIGHT"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1

    cnt = check("THREE", arrs, 0)
    for k in range(cnt):
        result += "3"
        for c in list("THREE"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1

    cnt = check("FIVE", arrs, 0)
    for k in range(cnt):
        result += "5"
        for c in list("FIVE"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1

    cnt = check("ONE", arrs, 0)
    for k in range(cnt):
        result += "1"
        for c in list("ONE"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1


    cnt = check("SEVEN", arrs, 0)
    for k in range(cnt):
        result += "7"
        for c in list("SEVEN"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1

    cnt = check("NINE", arrs, 0)
    for k in range(cnt):
        result += "9"
        for c in list("NINE"):
            if c in arrs and arrs[c] > 0:
                arrs[c] = arrs[c] -1

    res = list(result)
    res.sort()
    result = ''.join(res)
    print "CASE #" + str(index+1) + ": " + result
