
def swapStack(stack):
    newStack = []
    for one in stack:
        if one:
            newStack.append( False )
        else:
            newStack.append( True )
    
    return newStack
    

def solve(stack):
    BoolStack = map(lambda x : True if x =='+' else False,stack)
    
    last = BoolStack[0]
    ReducedBoolStack = [last,]
    for one in BoolStack[1:]:
        if last != one:
            ReducedBoolStack.append(one)
            last = one
        

    inversions = 0
    while len(set(ReducedBoolStack))!=1 or ReducedBoolStack[0]==False:
        tempRstack = list(ReducedBoolStack)
        
        cuttedLen = 0
        while tempRstack[-1]:
            tempRstack = tempRstack[:-1]
            cuttedLen += 1
        
            
        tempRstack = swapStack(tempRstack)
        inversions += 1

        if cuttedLen: 
            ReducedBoolStack = tempRstack + ReducedBoolStack[-cuttedLen:]
        else:
            ReducedBoolStack = tempRstack
        
    return inversions
        






