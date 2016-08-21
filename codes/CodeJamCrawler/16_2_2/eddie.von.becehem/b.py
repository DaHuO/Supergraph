from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

debug = True

# 1? 2? -> 19 20
# ?2? ??3 -> 023 023
# ? ?   -> 0 0
# ?5 ?0 -> 05 00

# ?1 ?2 -> 01 02
# ?5 ?0 -> 05 00
# ?5 10 -> 05 10  (pas 15 10)
# ?6 10 -> 06 10
# ?0 ?5 -> 00 05 
# 5? 4? -> 50 49
# 5 ?    -> 5 5


# savoir qui est plus grand (donc en partant de la gauche)
#     si droit plus grande: chaque ? de LEFT, prend grand, et chaque droit de RIGHT, prend petit
#     si gauche: chaque ? de LEFT, prend petit, et chaque droit de RIGHT, prend grand
#     si on sait pas: 
#         si ? en meme temps: prend 0
#         si un nombre a gauche

def enlarge(clist, char):
    rep = []
    if char != '?':
        for c in clist:
            rep.append(c * 10 + int(char))
    else:
        for c in clist:
            for d in range(10):
                rep.append(c * 10 + d)

    return rep

def abs(i):
    if i > 0:
        return i
    return 0 - i

def exhaust(c, j):
    
    clist = [0]
    for cchar in c:
        clist = enlarge(clist, cchar)

    jlist = [0]
    for jchar in j:
        jlist = enlarge(jlist, jchar)

    diff = []
    for cchar in clist:
        for jchar in jlist:
            diff.append((abs(cchar-jchar), cchar, jchar))

    diff.sort()
    repc = str(diff[0][1])
    repj = str(diff[0][2])
    while len(repc) < len(c):
        repc = "0" + repc
    while len(repj) < len(c):
        repj = "0" + repj

    return repc + " " + repj
    
def ans(c, j):

    crep = ""
    jrep = ""
    whoIsGreater = None

    for i in range(len(C)):
        cchar = c[i]
        jchar = j[i]

        if whoIsGreater == 'c':
            if cchar == '?':
                cchar = '0'
            if jchar == '?':
                jchar = '9'
        elif whoIsGreater == 'j':
            if cchar == '?':
                cchar = '9'
            if jchar == '?':
                jchar = '0'
        else:
            if cchar != '?' and jchar != '?':
                # Nothing
                if int(cchar) > int(jchar):
                    whoIsGreater = 'c'
                elif int(cchar) < int(jchar):
                    whoIsGreater = 'j'
            elif cchar == '?' and jchar == '?':
                if i == len(C) - 1:
                    cchar = '0'
                    jchar = '0'
                else:
                    if c[i+1] == '?' or j[i+1] == '?':
                        cchar = '0'
                        jchar = '0'
                    elif (10 + int(c[i+1]) - int(j[i+1]) < 5):
                        cchar = '1'
                        jchar = '0'
                    else:
                        cchar = '0'
                        jchar = '0'

            elif cchar == '?':
                cchar = jchar
            elif jchar == '?':
                jchar = cchar

        crep += cchar
        jrep += jchar

    return crep + ' ' + jrep

T = int(stdin.readline())
    
for i in range(1,T+1):

    C, J = stdin.readline().split()
    
    print "Case #" + str(i) + ":", 

    # print ans(C, J)
    print exhaust(C, J)

