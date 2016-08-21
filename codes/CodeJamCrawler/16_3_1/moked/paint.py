import math
import re
import numpy as np
import sys

f = open("A-large.in.txt")
fw = open("output.txt", 'w+')

first_line = f.readline()
T = int(first_line)

def checkMaj(p):

    for i in xrange(0, len(p)):

        sen = p[i]
        sumOthers = 0

        for j in xrange(0, len(p)):

            if j == i:
                continue

            sumOthers += p[j]

            pass 

        if sen > sumOthers:
            return False
        pass 

    return True
    pass

def chechFin(p):
    for i in xrange(0, len(p)):
        if p[i] != 0:
            return False
        pass 

    return True
    pass

for x in xrange(0, T):
    first_line = f.readline()
    N = int(first_line) # no of parties

    first_line = f.readline()
    numbers = first_line.split()
    parties = []

    for i in xrange(0, len(numbers)):
        parties.append(int(numbers[i]))
        pass

    # found the parties
    fw.write(('Case #{0}:'.format(x + 1)))

    # totalParties = 0
    # biggest = 0
    # partiesDiff = []

    # for j in xrange(0, len(parties)):
    #     totalParties += int(parties[j])
    #     if int(parties[j]) > biggest:
    #         biggest = int(parties[j])
    #     pass

    # for j in xrange(0, len(parties)):
    #     partiesDiff.append(int(parties[j]) - biggest)
    #     pass

    finished = False
    while finished != True:

        totalParties = 0
        biggest = 0
        partiesDiff = []

        for j in xrange(0, len(parties)):
            totalParties += int(parties[j])
            if int(parties[j]) > biggest:
                biggest = int(parties[j])
            pass

        for j in xrange(0, len(parties)):
            partiesDiff.append(int(parties[j]) - biggest)
            pass

        partiesClone = parties
        firstBiggestIndex = -1
        for j in xrange(0, len(parties)):
            if parties[j] >= parties[firstBiggestIndex]:
                firstBiggestIndex = j
            pass

        secondBiggestIndex = -1
        for j in xrange(0, len(parties)):
            if parties[j] >= parties[secondBiggestIndex] and j != firstBiggestIndex:
                secondBiggestIndex = j
            pass

        if partiesClone[firstBiggestIndex] >= 2:
            partiesClone[firstBiggestIndex] -= 2
            if checkMaj(partiesClone) != True:
                partiesClone[firstBiggestIndex] += 2

                partiesClone[firstBiggestIndex] -= 1
                partiesClone[secondBiggestIndex] -= 1
                if checkMaj(partiesClone) != True:
                    partiesClone[secondBiggestIndex] += 1
                    fw.write((' {0}'.format(chr(firstBiggestIndex + 65))))
                else:  
                    fw.write((' {0}{1}'.format(chr(firstBiggestIndex + 65), chr(secondBiggestIndex + 65))))

            else:
                fw.write((' {0}{1}'.format(chr(firstBiggestIndex + 65), chr(firstBiggestIndex + 65))))

        else:
            partiesClone[firstBiggestIndex] -= 1
            partiesClone[secondBiggestIndex] -= 1
            if checkMaj(partiesClone) != True:
                partiesClone[secondBiggestIndex] += 1 
                fw.write((' {0}'.format(chr(firstBiggestIndex + 65))))
            else:
                fw.write((' {0}{1}'.format(chr(firstBiggestIndex + 65), chr(secondBiggestIndex + 65))))



        parties = partiesClone
        finished = chechFin(parties)

        print parties

        pass

    print partiesDiff

    fw.write('\n')

    pass

f.close()
fw.close()