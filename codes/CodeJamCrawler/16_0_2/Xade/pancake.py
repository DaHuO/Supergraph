from collections import deque

def flipTop(n, stack):
    tempQ = deque([])
    tempS = deque(stack)
    for i in range(n):
        tempQ.append(tempS.popleft())

    tempQ = change(tempQ)
    for i in range(n):
        tempS.appendleft(tempQ.pop())

    return list(tempS)


def change(stack):
    for i in range(len(stack)):
        if stack[i] == '+':
            stack[i] = '-'
        elif stack[i] == '-':
            stack[i] = '+'

    return stack


def checkComplete(iterator):
    return iterator[0] == '+' and len(set(iterator)) <= 1


'''
Search until I find the last negative then flip
continue until finished
'''
def findIndex(stack):
    previous = ''
    index = -1
    for i in range(len(stack)):
        if previous == '-' and stack[i] == '+':
            return i - 1
        if previous == '-' and stack[i] == '-':
            index = i
        previous = stack[i]

    if index == -1:
        return len(stack) - 1
    else:
        return index

def solve(stack):
    flips = 0

    while(not checkComplete(stack)):
        stack = flipTop(findIndex(stack) + 1, stack)
        flips += 1

    return flips


testcases = 0
output = open('output.txt', 'w')
with open('input.txt', 'r') as f:
    testcases = int(f.readline())
    count = 0
    for line in f:
        count += 1
        output.write('Case #' + str(count) + ': ' + str(solve(list(line.strip()))) + '\n')

output.close()