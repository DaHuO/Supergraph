##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(k,c,s):
    if c*s<k:
        return "IMPOSSIBLE"

    # set up list
    
    # every student can check C tiles of the original sequence
    tiles = []
    for i in range(0,k,c):

        # tiles to be checked
        l = [min(i+j,k-1) for j in range(c)]

        # compute tile position which must be G
        # (if at least one of tiles in l is G)
        tile = 0
        for j in range(c):
            tile += k**j * l[j]
        tiles.append(1+tile)

    return " ".join([str(item) for item in tiles])
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    k,c,s = [int(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(k,c,s)
    print('Case #'+str(t+1)+': '+str(result))

