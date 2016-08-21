#Code by Lilli Christoph 2016
#This dynamic algorithm was with much help from online sources below:
#http://www.necessaryandsufficient.net/2009/09/code-jam-2009-bribe-the-prisoners/
#I would have totally spent forever on the list dimension limits, etc

#!usr/bin/python


import sys

def flipper(numCakes, minFlips):
    #if(numCakes == 0):
        #indicates only a top '+' pancake left, no need to flip
     #   return 0
    #if(numCakes == 1):
        #indicates only a top '-' pancake left, flip it.
    #    return 1
    if(minFlips[numCakes] >= 0):
        #I've already calc it, so just return the answer
        return minFlips[numCakes]

    cheapest = 1<<30 #largest 32 bit signed int, apparently
    for i in range(numCakes):
        #if len of upper stack is odd, flipping changes the stack
        if((i+2) % 2) == 0:
            cheapest = min(cheapest, 1+ flipper(i, minFlips) +
                           flipper(numCakes-i-1, minFlips))
       #cheapest = min(cheapest, R[right+1] - R[left-1] -2 +
        #               minGold(left, i-1, minCost) +
         #              minGold(i+1, right, minCost))
    minFlips[numCakes] = cheapest
    return cheapest



bigStack = 100 #max S for large input
smallStack = 10 #max S for small input
#minFlips[x] is fewest flips I need to reorient a reduced stack of length x
#assuming lowest pancake I'm care about is '-' orientation
#x=0 indicates all pancakes face up   
minFlips = [-1 for j in range(bigStack+1)]
minFlips[0] = 0
minFlips[1] = 1


       
num_cases = int(sys.stdin.readline())
       
for i in range(num_cases):
    for line in sys.stdin.readline().split():
        raw_data = [x for x in line]
    myStack = []
    #collapse strings of '+' and '-' cakes
    #represent '-' as -1 and '+' and +1
    #print len(raw_data)

    #keep in mind stack was read in top to bottom
    #i want to reverse it because I'm a n00b
    if raw_data[-1] == '-':
            myStack.append(-1)
    for j in range(len(raw_data)-2, -1, -1):
        if raw_data[j] != raw_data[j+1]:
            #pancake section indicated by change in orientation
            if(len(myStack) == 0):
                myStack.append(-1)
                continue
            myStack.append(-1*myStack[-1])
            
    #print raw_data
    #print myStack, len(myStack)
 
    print 'Case #{}: {} '.format(i+1, flipper(len(myStack), minFlips))
