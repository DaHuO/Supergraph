import math

def checkPossible(k,c,s):
    return (math.ceil(k/c) <= s)

def findLocation(itemLocationArray,k): # k = length of initial sequence
    location = 0
    for i in range(len(itemLocationArray)):
        location += itemLocationArray[i]*(k**i)
    return location+1

def getTilePositions(k,c):
    tilePositions = []
    currentBranch = 0 #branch being eliminated at the instance
    while currentBranch != k:
        itemLocationArray = []
        for i in range(c):
            if currentBranch != k:
                itemLocationArray.append(currentBranch)
                currentBranch += 1
            else:
                itemLocationArray.append(k-1)
        location = findLocation(itemLocationArray,k) 
        tilePositions.append(location)
    return tilePositions 

file_object = open('D-small-attempt0.in','r')
file_object2 = open('output.txt','w')
t = int(file_object.readline().rstrip('\n'))
for _ in range(t):
    k,c,s = map(int,file_object.readline().rstrip('\n').split())
    isPossible = checkPossible(k,c,s)
    if not isPossible:
        file_object2.write('Case #'+str(_+1)+': IMPOSIBBLE\n')
        #print('IMPOSSIBLE') #working
    else: #continue
        tilePositions = getTilePositions(k,c)
        file_object2.write('Case #'+str(_+1)+': '+' '.join([str(x) for x in tilePositions])+'\n')
        #print(tilePositions)


