from itertools import groupby
import sys

memp = {}
memn = {}

def flipPositive(inp) :
    if len(inp) is 0 :
        return 0

    if len(inp) in memp:
        return memp[len(inp)]

    p = flipPositive(inp[1:])
    n = flipNegative(inp[1:])

    ch = inp[0][0]
 
    if p%2 is 1 : 
        if ch is '+' : 
            ch = '-'
        else : 
            ch = '+'
   
    if ch is '+':
        pv = p
    else : 
        pv = p + 1

    ch = inp[0][0]
 
    if n%2 is 1 : 
        if ch is '+' : 
            ch = '-'
        else : 
            ch = '+'
    
    if ch is '+':
        nv = n + 2
    else : 
        nv = n + 1 
    
    memp[len(inp)] = min(pv,nv)
    #print "Pos",inp,min(pv,nv),p,n
    return min(pv,nv)

def flipNegative(inp) :
    if len(inp) is 0 :
        return 0

    if len(inp) in memn:
        return memn[len(inp)]
    
    #print "n",inp
    p = flipPositive(inp[1:])
    n = flipNegative(inp[1:])

    ch = inp[0][0]
 
    if p%2 is 1 : 
        if ch is '+' : 
            ch = '-'
        else : 
            ch = '+'
    
    if ch is '-':
        pv = p + 2
    else : 
        pv = p + 1

    ch = inp[0][0]
 
    if n%2 is 1 : 
        if ch is '+' : 
            ch = '-'
        else : 
            ch = '+'
    
    if ch is '-':
        nv = n
    else : 
        nv = n + 1 
    
    memn[len(inp)] = min(pv,nv)
    return min(pv,nv)

w = int(sys.stdin.readline().strip())
i = 1
for line in sys.stdin:
    inp = ["".join(grp) for num, grp in groupby(line)]
    inp = inp[:len(inp)-1]
    proc = [(grp[0],len(grp)) for grp in inp]
    memp = {}
    memn = {}
    print "Case #"+str(i)+":",flipPositive(proc)
    i+=1

