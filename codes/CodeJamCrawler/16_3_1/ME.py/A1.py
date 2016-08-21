
##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(n,p):
    l = [[p[i],chr(65+i)] for i in range(n)]
    l.sort()
    l.reverse()
    p1,p2 = 0,1
    res = []
    while p1<n:
        l[p1][0] -= 1
        if p2<n:
            l[p2][0] -= 1
            res.append(l[p1][1]+l[p2][1])
        else:
            res.append(l[p1][1])

        if p2<n and l[p2][0]==0:
            p2 += 1
            
        if l[p1][0] == 0:
            p1 = p2
            p2 += 1
        
    res.reverse()
    return " ".join(res)
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    n = int(input())
    p = [int(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(n,p)
    print('Case #'+str(t+1)+': '+str(result))
    
