import numpy as np
import time
from scipy.linalg import circulant

#f = open('A-small-attempt0.in','r')
#g = open('A-small-attempt0.ou','w')

#f = open('A-small.in','r')
#g = open('A-small.ou','w')

f = open('A-large.in','r')
g = open('A-large.ou','w')


def inputToList(f):
    n = int(f.readline()[:-1])
    iL = []
    for k in range(n):
        l_k = f.readline()[:-1]
        iL += [[ord(x) for x in l_k]]
    return iL


iL = inputToList(f)


def solution(pat):
    n = max(pat)
    sol1 = ''
    sol2 = ''
    for k in range(len(pat)):
        if pat[k] == n:
            sol1 += chr(pat[k])
        else:
            sol2 += chr(pat[k])
    sol = sol1 + sol2
    return sol


def solution2(pat):
    new_pat = pat
    sol1 = ''
    sol2 = ''
    k = 1
    while k <> 0:
        sol11 = ''
        sol22 = ''
        n = max(new_pat)
        k = argmax(new_pat)
        for i in range(k, len(new_pat)):
            if new_pat[i] == n:
                sol11 += chr(pat[i])
            else:
                sol22 += chr(pat[i])
        new_pat = new_pat[:k]
        sol1 = sol1 + sol11
        sol2 = sol22 + sol2
    sol = sol1 + sol2
    return sol



def outputList(iL):
    oL = []
    for k in range(len(iL)):
        oL += [solution2(iL[k])]
	print k+1,'Done'
    return oL


oL = outputList(iL)


def outputListToString(oL):
    oS = ''
    for k in range(len(oL)):
        oS += 'Case #'+str(k+1)+': '+ str(oL[k])+'\n'
    return oS


oS = outputListToString(oL)


g.write(oS)


g.close()
