# Google code jam flipping pancakes

def flipStack(stack):
    # reverse order
    sstack = stack[::-1]
    # NOT
    sstack = ((sstack.replace('+','0')).replace('-','+')).replace('0','-')
    return(sstack)

        
T = int(input()) # read number of cases from stdin

for j in range(1,T+1):

    stack = str(input()) # read input string (python3)

    n = 0 # sequence: always flip top substack of equal pancakes
    while True:
        
        if len(stack) == 0: # catch "empty plates"
            break
        
        if stack[0] == '+':
            i = stack.find('-')
            if (i == -1):
                break
        else:
            i = stack.find('+')
            if (i == -1):
                n += 1
                break
            
        n+=1
        stack = stack[i::]
        
            
    print("Case #{}: {}".format(j,n)) # case result output
        
