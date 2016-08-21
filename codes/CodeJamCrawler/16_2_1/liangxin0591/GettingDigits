#!/usr/bin/python

import sys
import string


def gettingD(s):
    # built dic
    dic = {}
    for c in string.ascii_uppercase:
        dic[c] = 0
    for c in s:
        dic[c] = dic[c] + 1
    list = []
    
    # zeros
    nZ = dic['Z']
    dic['Z'] -= nZ
    dic['E'] -= nZ
    dic['R'] -= nZ
    dic['O'] -= nZ
    for i in range(0, nZ):
        list.append(0)
    
    # twos
    nW = dic['W']
    dic['T'] -= nW
    dic['W'] -= nW
    dic['O'] -= nW
    for i in range(0, nW):
        list.append(2)

    # eights
    nG = dic['G']
    for c in 'EIGHT':
        dic[c] -= nG
    for i in range(0, nG):
        list.append(8)
    
    # three
    nH = dic['H']
    for c in 'THREE':
        dic[c] -= nH
    dic['E'] -= nH
    for i in range(0, nH):
        list.append(3)

    # four
    nR = dic['R']
    for c in 'FOUR':
        dic[c] -= nR
    for i in range(0, nR):
        list.append(4)

    # one
    nO = dic['O']
    for c in 'ONE':
        dic[c] -= nO
    for i in range(0, nO):
        list.append(1)

    # five
    nF = dic['F']
    for c in 'FIVE':
        dic[c] -= nF
    for i in range(0,nF):
        list.append(5)

    # seven
    nV = dic['V']
    for c in 'SEVEN':
        dic[c] -= nV
    dic['E'] -= nV
    for i in range(0, nV):
        list.append(7)

    # six
    nS = dic['S']
    for c in 'SIX':
        dic[c] -= nS
    for i in range(0, nS):
        list.append(6)

    # nine
    nI = dic['I']
    for c in 'NINE':
        dic[c] -= nI
    dic['N'] -= nI
    for i in range(0,nI):
        list.append(9)

    list.sort()
    slist = []
    for n in list:
        slist.append(str(n))

    s = "".join(slist)
    return s

if __name__ == "__main__":
   t = int(raw_input())
   for i in range(1, t + 1):
       S = raw_input()
       s = gettingD(S)
       print("Case #" + str(i) + ": " + s)


