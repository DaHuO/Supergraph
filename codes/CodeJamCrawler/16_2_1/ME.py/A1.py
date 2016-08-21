##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(s):
    Digits = [(0,"ZERO"),
              (2,"TWO"),
              (6,"SIX"),  
              (8,"EIGHT"),
              (7,"SEVEN"),
              (5,"FIVE"),
              (4,"FOUR"),
              (3,"THREE"),
              (9,"NINE"),
              (1,"ONE")
              ]
    
    s = list(s)
    result = []
    for digit,digitWord in Digits:
        while True:
            testS = list(s)
            ok = True
            for letter in digitWord:
                if letter in testS:
                    testS.remove(letter)
                else:
                    ok = False
            if ok:
                result.append(digit)
                s = testS
            else:
                break

    assert(s==[])
        
    result.sort()
    return "".join([str(item) for item in result])
    
                    
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
