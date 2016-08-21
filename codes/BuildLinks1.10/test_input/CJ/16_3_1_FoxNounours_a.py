#/usr/bin/python3

import sys

inputFile = open("input", "r")
outputFile = open("output", "w")
caseNb = 1

inputLine = inputFile.readline()
T = int(inputLine)

for inputLine in inputFile :

    N = int(inputLine)
    inputLine = inputFile.readline()
    P = inputLine.split()
    PCount = {}
    big1 = None
    big2 = None
    result = ""
    slice = False

    for i in range(0,len(P)) :
        P[i] = int(P[i])
        Pname = chr(ord('A')+i)
        PCount[Pname] = int(P[i])
        if big1 == None :
            big1 = Pname
        elif big2 == None :
            if P[i] >= PCount[big1] :
                big2 = big1
                big1 = Pname
            else :
                big2 = Pname
        elif P[i] >= PCount[big1] :
            big2 = big1
            big1 = Pname
        elif P[i] >= PCount[big2] :
            big2 = Pname

    while PCount[big1] > PCount[big2]+1 :
        result += big1+big1+' '
        PCount[big1] -= 2

    if PCount[big1] > PCount[big2] :
        result += big1
        PCount[big1] -= 1
        slice=True
        
    for K,V in PCount.items() :
        if K != big1 and K != big2 :
            if slice :
                result += K+' '
                V -= 1
            for i in range(0,V//2) :
                result += K+K+' '
            if V % 2 == 1 :
                result += K
                slice = True
            else :
                slice = False

    if slice :
        result += ' '
    for i in range(0,PCount[big1]) :
        result += big1+big2+' '
    
    outputFile.write("Case #{0}: {1}\n".format(caseNb, "".join(result)));

    caseNb += 1

inputFile.close()
outputFile.close()
