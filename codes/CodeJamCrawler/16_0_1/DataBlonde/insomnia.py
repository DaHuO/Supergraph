# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:11:51 2016

@author: marinasergeeva
"""
from sys import stdin
#import re

def getMaxNumber(number):
    if number == 0:
        return "INSOMNIA"
#    if reg20s.match(str(number)):
#        return str(45 * number)
    curMult = 1
    curSet = set()
    while len(curSet) < 10:
        curNumber = number * curMult
        curSet.update(set([int(s) for s in str(curNumber)]))
        curMult += 1
    return str(curNumber)

        
        

def main():
    numCases = int(stdin.readline().strip())
#    reg20s = re.compile("(20+)*2*$") 
    for i in range(1, numCases + 1):        
        number = int(stdin.readline().strip())
        print "Case #{0}: ".format(i) + getMaxNumber(number)
        
if __name__ == "__main__":
    main()