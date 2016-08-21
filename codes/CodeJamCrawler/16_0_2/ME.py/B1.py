##            
## PROBLEM SOLVING ALGORITHM 
##
## recursive approach from bottom (assume optimality)
##
def solve(s):
    # done
    if s=="":
        return 0

    # pancake ok
    if s[-1]=="+":
        return solve(s[0:len(s)-1])
    s2 = ""

    # have to flip, solve inverted problem for remaining stack
    for item in s:
        s2 += chr(88-ord(item))
    return 1+solve(s2)
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    s = input().rstrip()
        
    ## solve and print result
    result = solve(s)
    print('Case #'+str(t+1)+': '+str(result))
