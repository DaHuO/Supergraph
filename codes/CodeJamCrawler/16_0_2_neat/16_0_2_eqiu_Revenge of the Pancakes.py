def flip(stack, num):
    """
    :type num: int
    :type stack: list
    """
    temp = stack[:num]
    stack = stack[num:]
    temp = list(reversed(temp))
    for i in range(num):
        if temp[i] == '+':
            temp[i] = '-'
        else:
            temp[i] = '+'
    return temp + stack

f = open("B-large.in", "r")
output = open("OUTPUT.txt", "w")

numCases = int(f.readline())

for case in range(1, numCases+1):
    stackStr = f.readline().strip()
    length = len(stackStr)
    stack = list(stackStr)
    flips = 0
    lastBlank = 0
    if '-' not in stack:
        output.write("case #" + str(case) + ": 0\n")
        continue
    while '-' in stack:
        for i in reversed(range(length)):
            if stack[i] == '-':
                lastBlank = i
                break
        if '+' in stack[:lastBlank]:
            lastFirstFace = -1
            for j in range(lastBlank + 1):
                if stack[j] == '+':
                    lastFirstFace = j
                if stack[j] == '-':
                    break
            if lastFirstFace > -1:
                stack = flip(stack, lastFirstFace + 1)
                flips += 1
        if '-' in stack:
            stack = flip(stack, lastBlank + 1)
            flips += 1
    output.write("case #" + str(case) + ": " + str(flips) + "\n")
f.close()
output.close()