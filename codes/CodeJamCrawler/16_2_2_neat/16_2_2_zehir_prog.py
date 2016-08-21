#! /usr/bin/env python3

def fill(s):
    res = []
    for i in range(len(s)):
        if s[i] == '?':
            for k in range(10):
                for post in fill(s[i+1:]):
                    res.append(s[:i] + str(k) + post)
            return res
    return [s]

def f(code, jam):
    codelist = fill(code)
    jamlist = fill(jam)
    dists = []
    bestcode = codelist[0]
    bestjam = jamlist[0]
    mindist = abs(int(bestcode) - int(bestjam))
    for fcode in codelist:
        for fjam in jamlist:
            icode = int(fcode)
            ijam = int(fjam)
            if abs(icode - ijam) < mindist or (
                abs(icode - ijam) == mindist and (icode < int(bestcode) or (
                    icode == int(bestcode) and ijam < int(bestjam)))):
                mindist = abs(icode - ijam)
                bestcode = fcode
                bestjam = fjam
    return bestcode + ' ' + bestjam

t = int(input())
for i in range(1, t + 1):
    code, jam = input().split(' ')
    print('Case #{}: {}'.format(i, f(code, jam)))
