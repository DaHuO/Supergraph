import sys

##            
## PROBLEM SOLVING ALGORITHM 
##

## brute force, won't work for large problem

def solutions(s):
    l = []
    n = s.count("?")
    for i in range(10**n):
        c = ("00"+str(i))[-n:]
        r = ""
        for ch in s:
            if ch=="?":
                r += c[0]
                c = c[1:]
            else:
                r += ch
        l.append(r)
    l.sort()
    return l
        
def solve(c,j):
    sc = solutions(c)
    sj = solutions(j)

    diff = None
    for pj in sj:
        for pc in sc:
            if diff==None or abs(int(pj)-int(pc))<diff:
                diff = abs(int(pj)-int(pc))
                res = pc,pj
                
    return res[0]+" "+res[1]
                 
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    c,j = input().rstrip().split()
        
    ## solve and print result
    result = solve(c,j)
    print('Case #'+str(t+1)+': '+str(result))

    ## progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)
