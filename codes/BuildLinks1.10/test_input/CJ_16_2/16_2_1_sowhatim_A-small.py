#!/usr/bin/env python3
def cut(L, ele, cnt):
    for _ in range(cnt):
        for i in ele:
            L.remove(i)
    return L

cases = int(input())
for case in range(1, cases+1):
    inpt = [i for i in input()]
    zerocnt = inpt.count('Z')
    cut(inpt, 'ZERO', zerocnt)
    twocnt = inpt.count('W')
    cut(inpt, 'TWO', twocnt)
    sixcnt = inpt.count('X')
    cut(inpt, 'SIX', sixcnt)
    eightcnt = inpt.count('G')
    cut(inpt, 'EIGHT', eightcnt)
    fourcnt = inpt.count('U')
    cut(inpt, 'FOUR', fourcnt)
    threecnt = inpt.count('R')
    onecnt = inpt.count('O')
    sevencnt = inpt.count('S')
    cut(inpt, 'SEVEN', sevencnt)
    fivecnt = inpt.count('V')
    cut(inpt, 'FIVE', fivecnt)
    ninecnt = inpt.count('I')
    number = ''
    for i in range(zerocnt):
        number += '0'
    for i in range(onecnt):
        number += '1'
    for i in range(twocnt):
        number += '2'
    for i in range(threecnt):
        number += '3'
    for i in range(fourcnt):
        number += '4'
    for i in range(fivecnt):
        number += '5'
    for i in range(sixcnt):
        number += '6'
    for i in range(sevencnt):
        number += '7'
    for i in range(eightcnt):
        number += '8'
    for i in range(ninecnt):
        number += '9'
    print ("Case #{}: {}".format(case, number))
