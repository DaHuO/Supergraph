#python3

import math

def flipcake(cake):
    if cake == '+':
        return '-'
    return '+'    

def flip(cakes, idx):
    newcakes = cakes[:]
    for i in range(idx):
        newcakes[i] = flipcake(cakes[idx-1-i])
    return newcakes

def solve(cakes):
    if cakes[-1] == '-':
        if cakes[0] == '-':
            return 1 + solve(flip(cakes,len(cakes)))
        happyidx = -1
        for i in range(len(cakes)-2,-1,-1):
            if cakes[i] == '+':
                happyidx = i
                break
        return 1 + solve(flip(cakes,happyidx+1))
    else:
        blankidx = -1
        for i in range(len(cakes)-1,-1,-1):
            if cakes[i] == '-':
                blankidx = i
                break
        if blankidx == -1:
            return 0
        return solve(cakes[:i+1])
                

inputfilename = "B-large.in.txt"
outputfilename = "B-large.out"

outputf = open(outputfilename, 'w')
with open(inputfilename, 'r') as f:
    T = int(f.readline())
    for i in range(1,T+1):
        S = f.readline().strip()
 
        flips = solve(list(S))
        
        outputf.write("Case #" + str(i) + ": " + str(flips) + "\n")
    
    
outputf.close()
