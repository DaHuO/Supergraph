# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:03:46 2016

@author: marinasergeeva
"""

from sys import argv
import heapq

def getFile(argv):
    if len(argv) < 2:
        raise ValueError
    if argv[1] == "t":
        return open("test.txt", "r"), open("testRes.txt", "w")
    if argv[1] == "s":
        return open("A-small-attempt1.in", "r"), open("smallRes.txt", "w")
    else:
        return open("A-large.in", "r"), open("largeRes.txt", "w")

def getMaxParty(parties, partiesOrder):
    if partiesOrder == []:
        partiesOrder = [(-v, k) for (k, v) in parties.iteritems()]
        heapq.heapify(partiesOrder)
    (num, p) = heapq.heappop(partiesOrder)
    if len(partiesOrder) == 2 and num <= -2:
        (num1, p1) = heapq.heappop(partiesOrder)
        others = partiesOrder[0][0] + num + 2
        heapq.heappush(partiesOrder, (num1, p1))
        if num1 < others:
           heapq.heappush(partiesOrder, (num + 1, p)) 
        return (p, 1)
    if num < -2:
        heapq.heappush(partiesOrder, (num + 2, p))
        return (p, 2)
    if num == -2:
        return (p, 2)
    return (p, 1)
    

def getResult(numbers):
    parties = {chr(ord("A") + i): number for (i, number) in enumerate(numbers)}
    partiesOrder = []
    res = []
    while len(parties.keys()) > 2:
        (p, num) = getMaxParty(parties, partiesOrder)
        parties[p] -= num
        res.append("".join(p for i in range(num)))
        if parties[p] == 0:
            del parties[p]

    count = parties.values()[0]
    for i in range(count):
        res.append("".join(parties.keys()))
    return " ".join(res)
        
        

def main(argv):
    iFile, oFile = getFile(argv)
    numCases = int(iFile.readline().strip())
    for i in range(1, numCases + 1):    
        iFile.readline()
        numbers = [int(el) for el in iFile.readline().strip().split()]
        oFile.write("Case #{0}: ".format(i) + getResult(numbers) + "\n")
    iFile.close()
    oFile.close()
        
if __name__ == "__main__":
    main(argv)