#python3

import math

def digits(n):
    if n < 10:
        return [n]
    k = int(math.ceil(math.log10(n)))
    if n == 10**k:
        return [1] + [0]*k

    return [(n//10**i)%10 for i in range(k)]

def solve(N):
    if N == 0:
        return "INSOMNIA"
    seendigits = [False]*10
    lastnumber = N
    
    while True:
        d = digits(lastnumber)
        for digit in d:
            seendigits[digit] = True
        if all(seendigits):
            return lastnumber
        
        lastnumber += N 

inputfilename = "A-large.in"
outputfilename = "A-large.out"

outputf = open(outputfilename, 'w')
with open(inputfilename, 'r') as f:
    T = int(f.readline())
    for i in range(1,T+1):
        N = int(f.readline())
 
        lastnumber = solve(N)
        
        outputf.write("Case #" + str(i) + ": " + str(lastnumber) + "\n")
    
    
outputf.close()
