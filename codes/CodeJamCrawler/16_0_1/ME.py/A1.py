##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(N):
    if N==0:
        return "INSOMNIA"
    digits = [False for _ in range(10)]
    n = N
    while True:
        for digit in str(n):
            digits[int(digit)] = True
        
        if not (False in digits):
            return n
        n += N
        
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    N = int(input())
        
    ## solve and print result
    result = solve(N)
    print('Case #'+str(t+1)+': '+str(result))
