'''
Created on 30 de abr. de 2016

@author: Marcelo
'''

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())


def solve(S,N):
    S = list(S)
    
    R = list()
    
    zeros = S.count("Z")
    for i in range(zeros):
        R.append(0)
        for l in N[0]:
            p = S.index(l) 
            del(S[p]) 
            
    twos = S.count("W")
    for i in range(twos):
        R.append(2)
        for l in N[2]:
            p = S.index(l) 
            del(S[p])  
            
    fours = S.count("U")
    for i in range(fours):
        R.append(4)
        for l in N[4]:
            p = S.index(l) 
            del(S[p])        
              
    sixes = S.count("X")
    for i in range(sixes):
        R.append(6)
        for l in N[6]:
            p = S.index(l) 
            del(S[p])  
            
    eigths = S.count("G")
    for i in range(eigths):
        R.append(8)
        for l in N[8]:
            p = S.index(l) 
            del(S[p])   
            
    ones = S.count("O")
    for i in range(ones):
        R.append(1)
        for l in N[1]:
            p = S.index(l) 
            del(S[p])  
            
    threes = S.count("T")
    for i in range(threes):
        R.append(3)
        for l in N[3]:
            p = S.index(l) 
            del(S[p]) 
            
            
    fives = S.count("F")
    for i in range(fives):
        R.append(5)
        for l in N[5]:
            p = S.index(l) 
            del(S[p]) 
            
            
    sevens = S.count("S")
    for i in range(sevens):
        R.append(7)
        for l in N[7]:
            p = S.index(l) 
            del(S[p])   
            
    nines = S.count("N")/2
    for i in range(nines):
        R.append(9)
        for l in N[9]:
            p = S.index(l) 
            del(S[p])              
                           
    R.sort()        
    return ''.join(str(x) for x in R)


_T = readint()
for t in range(1, _T+1):

    S = raw_input()
    N = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]
    
    r = solve(S,N)
    
    
    print 'Case #%i:'%(t), r