numberOfCases = input()

pancakeList = []

for i in range(numberOfCases):
    pancakeList.append(list(raw_input()))

def pancakeFlipper(pancakeStack,lengthOriginal,sign):
    newLength = lengthOriginal - len(pancakeStack)
    newSigns = sign*newLength
    newSigns = list(newSigns)
    pancakeStack = newSigns + pancakeStack
    return pancakeStack
    
def pancakesSorter(pancakeStack):
    #print 'Function ran'
    #firstPancake = pancakeStack[0]
    lengthOfStack = len(pancakeStack)
    turns = 0
    while '-' in pancakeStack:
        #print 'Running'
        ##print pancakeStack, 'with %d turns' % turns##
        for values in range(lengthOfStack):
            firstPancake = pancakeStack[0]
            if '+' not in pancakeStack:
                turns += 1
                pancakeStack = '+'*lengthOfStack
                pancakeStack = list(pancakeStack)
                ##print pancakeStack, 'with %d turns' % turns##
            
                #print 'First pancake accomplished'
            else:
                #print 'Running the else statement'
                if pancakeStack[values] == firstPancake:
                    #print 'Checked if they were equal'
                    pass
                else:
                    sign = pancakeStack[values]
                    pancakeStack = pancakeStack[values:]
                    #print pancakeStack, lengthOfStack, firstPancake
                    pancakeStack = pancakeFlipper(pancakeStack,lengthOfStack,sign)
                    turns += 1
    return turns

for i in range(numberOfCases):
    pancakeStack = pancakeList[i]
    numberOfTurns = pancakesSorter(pancakeStack)
    print "Case #%d: %d" % (i+1, numberOfTurns)
                
                    