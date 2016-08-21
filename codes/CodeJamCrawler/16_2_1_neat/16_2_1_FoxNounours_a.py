#/usr/bin/python3

import sys

inputFile = open("input", "r")
outputFile = open("output", "w")
caseNb = 1

inputLine = inputFile.readline()
T = int(inputLine)

for inputLine in inputFile :

    #here
    result = []
    L = sorted(inputLine[:-1])

    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    
    # 0 2 4 6
    for c in L :
        if c ==  'Z' :
            c0 += 1
            result.append('0')
        elif c == 'W' :
            c2 += 1
            result.append('2')
        elif c == 'U' :
            c4 += 1
            result.append('4')
        elif c == 'X' :
            c6 += 1
            result.append('6')

    for i in range(0,c0) :
        L.remove('Z')
        L.remove('E')
        L.remove('R')
        L.remove('O')

    for i in range(0,c2) :
        L.remove('T')
        L.remove('W')
        L.remove('O')

    for i in range(0,c4) :
        L.remove('F')
        L.remove('O')
        L.remove('U')
        L.remove('R')

    for i in range(0,c6) :
        L.remove('S')
        L.remove('I')
        L.remove('X')

    # 3 5
    for c in L :
        if c == 'F' :
            c5 += 1
            result.append('5')
        elif c == 'R' :
            c3 += 1
            result.append('3')

    for i in range(0,c5) :
        L.remove('F')
        L.remove('I')
        L.remove('V')
        L.remove('E')

    for i in range(0,c3) :
        L.remove('T')
        L.remove('H')
        L.remove('R')
        L.remove('E')
        L.remove('E')

    # 7 8
    for c in L :
        if c == 'V' :
            c7 += 1
            result.append('7')
        elif c == 'H' :
            c8 += 1
            result.append('8')

    for i in range(0,c7) :
        L.remove('S')
        L.remove('E')
        L.remove('V')
        L.remove('E')
        L.remove('N')

    for i in range(0,c8) :
        L.remove('E')
        L.remove('I')
        L.remove('G')
        L.remove('H')
        L.remove('T')

    # 9 1
    for c in L :
        if c == 'I' :
            c9 += 1
            result.append('9')
        elif c == 'O' :
            c1 += 1
            result.append('1')

    for i in range(0,c1) :
        L.remove('O')
        L.remove('N')
        L.remove('E')

    for i in range(0,c9) :
        L.remove('N')
        L.remove('I')
        L.remove('N')
        L.remove('E')

    print(L)
    
    result.sort()
    outputFile.write("Case #{0}: {1}\n".format(caseNb, "".join(result)));

    caseNb += 1

inputFile.close()
outputFile.close()
