# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:32:35 2016

@author: marinasergeeva
"""
from sys import stdin

def pointToNumber(point, lengthOriginalSequence):
    res = 0
    for el in point[::-1]:
        res  = res * lengthOriginalSequence + el
    return res + 1

def getElementsToCheck(lengthOriginalSequence, level, elementsToCheck):
#    dimension = level
    pointsToCheck = []
    curPoint = []
    for i in range(lengthOriginalSequence):
        curPoint.append(i)
        if len(curPoint) == level:
            pointsToCheck.append(curPoint)
            curPoint = []
    if curPoint != []:
        pointsToCheck.append(curPoint)
    if len(pointsToCheck) > elementsToCheck:
        return "IMPOSSIBLE"
    return " ".join([str(pointToNumber(point, lengthOriginalSequence)) for point in pointsToCheck])
    
def main():
    numCases = int(stdin.readline().strip())
    for i in range(1, numCases + 1):        
        [lengthOriginalSequence, level, elementsToCheck] = [int(s) for s in stdin.readline().strip().split()]
        print "Case #{0}: ".format(i) + getElementsToCheck(lengthOriginalSequence, level, elementsToCheck)    
        
if __name__ == "__main__":
    main()