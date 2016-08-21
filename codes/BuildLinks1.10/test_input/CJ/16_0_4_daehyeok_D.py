from __future__ import print_function
import logging
import copy
import sys
import math

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

#def solve(firstLine):
def getLidxs(n, length):
    base2 = bin(n)[2:].zfill(length)
    lSet = set()
    for idx, ch in enumerate(base2):
        if ch == '1':
            lSet.add(idx)
            
    return lSet

def getNextLidxs(initLset, lset, length):
    newSet = set()
    for x in initLset:
        for y in lset:
            newSet.add(length * x + y)
            
    return newSet

def getMutatedLidxs(n,k, c):
    initlSet = getLidxs(n, k)
    lSet= copy.copy(initlSet)
    length = k
    for j in range(c-1):
        lSet = getNextLidxs(initlSet, lSet, length)
        length *= k

    return lSet
        
        
def solve(line):
    k,c,s = line[0], line[1], line[2]

    if k <= s :
        return range(1,k+1)
        
    lDict = {}
    lastNum = int(math.pow(2,k))
    for n in range(1,lastNum-1):
        log("mutation!")
        lSet= getMutatedLidxs(n,k,c)
        lDict[n] =  lSet

    anserList = []
    finalLength = int(math.pow(k,c))
    
    for i in range(s):
        log("mutation")
        countList = [1] * finalLength
        countDict = [{}] * finalLength
        for n, e in lDict.items():
            for j in e:
                countList[j] += 1
                countDict[j][n] = lDict[n] 

        
        for n in anserList:
            countList[n-1] = sys.maxsize
            
        minLength = min(countList)
        minIdx = countList.index(minLength)
        anserList.append(minIdx+1)

        if minLength <= 1 or len(anserList) == k:
            return anserList

        lDict = countDict[minIdx]

    return []

def main():
    t = int(input())
    
    for i in range(t):
        line = input().split()
        line = list(map(int, line))
        print("Case #%d: " % (i + 1)  , end="")
        a = solve(line)

        if len(a) == 0:
            print("IMPOSSIBLE")
        else:
            print(" ".join(str(x) for x in a))


def log(*message):
    logging.debug(message)
    
if __name__ == "__main__":
    main()
    

solve([53,5,53])
