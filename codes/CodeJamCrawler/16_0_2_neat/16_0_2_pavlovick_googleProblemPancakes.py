__author__ = 'pavlovick'


MAX_TURN=100

def firstOccerence(stack):
    running = True
    idx = 0
    while running and idx<len(stack)-1:
        thiselem, nextelem = stack[idx], stack[idx+1]
        if thiselem != nextelem:
            running=False
        else:
            idx = idx + 1
    return idx

def opposite(element):
    if element == '+':
        return '-'
    else:
        return '+'

def turnPancakes(pancakes, depth):
    for idx in range(0,depth+1):
        pancakes[idx]= opposite(pancakes[idx])
    return pancakes

def isStackReady(pancakesList):
    if '-' in pancakesList:
        return False
    else:
        return True


def pancakesReady(pancakes):
    pancakesList = list(pancakes)
    countTurn = 0
    while not isStackReady(pancakesList) and countTurn < MAX_TURN:
        depth = firstOccerence(pancakesList)
        pancakesList = turnPancakes(pancakesList, depth)
        countTurn = countTurn + 1
    if countTurn < MAX_TURN:
        return countTurn
    else:
        return 'IMPOSSIBLE'


solution = open('pancakes.txt', 'w')
with open('test.txt') as f:
    N= int(f.readline())
    count = 1
    for pancakes in f.read().splitlines():
        turnCount = pancakesReady(pancakes)
        newLine = 'Case #'+ str(count) +': '+ str(turnCount) +'\n'
        solution.write(newLine)
        count +=1

