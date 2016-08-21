import sys

##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(n,l):
    # brute force (will not work for large problem)

    res = 0
    for test in range(2**n):
        fakeList = [((test>>i)&1)==1 for i in range(n)]

        nonFakes0 = [l[i][0] for i in range(n) if fakeList[i]==False]
        nonFakes1 = [l[i][1] for i in range(n) if fakeList[i]==False]

        ok = True
        for i in range(n):
            if fakeList[i]:
                if (l[i][0] not in nonFakes0) or \
                   (l[i][1] not in nonFakes1):
                    ok = False
                    break
        if ok:
            res = max(res, fakeList.count(True))
            
    return res
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    n = int(input())
    l = [input().rstrip().split() for _ in range(n)]
        
    ## solve and print result
    result = solve(n,l)
    print('Case #'+str(t+1)+': '+str(result))

    ## progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)
