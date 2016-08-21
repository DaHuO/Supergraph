
def allFlipped(stack):
    for i in range(len(stack)):
        if stack[i] == '-':
            return False
    return True

def flip(val):
    if val == '+':
        return '-'
    else:
        return '+'

def findFlipPoint(stack):
    for i in range(1, len(stack)):
        if stack[i - 1] != stack[i]:
            return i
    return len(stack)

def flipStack(stack, point):
    flipped = []
    for i in range(point):
        flipped.insert(0, flip(stack[i]))
    for i in range(point, len(stack)):
        flipped.append(stack[i])
    return flipped

numTests = int(input())
for t in range(1, numTests + 1):
    numFlips = 0
    stack = input()
    while allFlipped(stack) == False:
        numFlips += 1
        flipPoint = findFlipPoint(stack)
        stack = flipStack(stack, flipPoint)
    print("Case #" + str(t) + ": " + str(numFlips))
