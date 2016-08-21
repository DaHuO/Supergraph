# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

def getANS(line):
    dic={}
    for s in line:
        if s in dic:
            dic[s]+=1
        else:
            dic[s]=1
    
    
    
    outstr=""
    
    if "Z" in dic:
        temp=dic["Z"]
        if temp >0:
            dic["Z"]-=temp
            dic["E"]-=temp
            dic["R"]-=temp
            dic["O"]-=temp
            outstr+= "0"*temp
        
    if "W" in dic:
        temp=dic["W"]
        if temp>0:
            dic["T"]-=temp
            dic["W"]-=temp
            dic["O"]-=temp
            outstr+= "2"*temp
    if "U" in dic:
        temp=dic["U"]
        if temp>0:
            dic["F"]-=temp
            dic["O"]-=temp
            dic["U"]-=temp
            dic["R"]-=temp
            outstr+= "4"*temp
    if "X" in dic:    
        temp=dic["X"]
        if temp>0:
            dic["S"]-=temp
            dic["I"]-=temp
            dic["X"]-=temp
            outstr+= "6"*temp
    if "G" in dic:
        temp=dic["G"]
        if temp>0:
            dic["E"]-=temp
            dic["I"]-=temp
            dic["G"]-=temp
            dic["H"]-=temp
            dic["T"]-=temp
            outstr+= "8"*temp
    
    if "O" in dic:
        temp=dic["O"]
        if temp>0:
            dic["O"]-=temp
            dic["N"]-=temp
            dic["E"]-=temp
            outstr+= "1"*temp
    if "T" in dic:  
        temp=dic["T"]
        if temp>0:
            dic["T"]-=temp
            dic["H"]-=temp
            dic["R"]-=temp
            dic["E"]-=2*temp
            outstr+= "3"*temp
    if "F" in dic:
        temp=dic["F"]
        if temp>0:
            dic["F"]-=temp
            dic["I"]-=temp
            dic["V"]-=temp
            dic["E"]-=temp
            outstr+= "5"*temp
    if "S" in dic:
        temp=dic["S"]
        if temp>0:
            dic["S"]-=temp
            dic["E"]-=2*temp
            dic["V"]-=temp
            dic["N"]-=temp
            outstr+= "7"*temp
    if "I" in dic:
        temp=dic["I"]
        outstr+= "9"*temp
    return ''.join(sorted(outstr))


result =[]
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
num_cases=int(lines[0])

for i in range(1,len(lines)):
    temp= "Case #" + str(i)+ ": " + str( getANS(lines[i]))
        
    result.append(temp)  
    
out=open(sys.argv[1]+"_ans.txt","w+")
out.write("\n".join(result))
out.close()


    