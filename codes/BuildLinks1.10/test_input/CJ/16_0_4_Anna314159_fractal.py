#!/usr/bin/python

import numpy as np
import math
import sympy as sp

# if S>=K: look at the first K/S tiles --> must be the original pattern or only gold
# if S==K-1: look at position 2 .. end --> position 1 must be tile of the original pattern (G--> 2 is also G)
def findGold(i, K, C, S, outFile): 
    pos=[]
    if S>=K: 
        pos=range(1,K+1)
    elif S==K-1: 
        pos=range(2,K+1)
    else: 
        pos=["IMPOSSIBLE"]
    outFile.write("Case #"+str(i+1) +": " + " ".join(map(str,pos)) + "\n")
    



inFile=open('fractInput.txt', 'r')
outFile=open('fractOutput.txt', 'w')

nrLines = int(inFile.readline())

for i, line in enumerate(inFile):
    numbers=map(int, line.split())
    K=numbers[0] # nr of tiles in the original pattern
    C=numbers[1] # complexity
    S=numbers[2] # nr of students
    findGold(i, K, C, S, outFile)
inFile.close()
outFile.close()
