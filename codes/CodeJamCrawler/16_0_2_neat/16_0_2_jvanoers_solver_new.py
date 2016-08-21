import os, sys

if not len(sys.argv) > 1:
    print("Enter input")
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print("File not found")
    sys.exit(1)

numberOfLines = 0
data = []
with open(sys.argv[1], 'r') as f:
    z = 0
    for i, line in enumerate(f):
        if i == 0:
            numberOfLines = int(line)
        else:
            data.append(line)
            if z > numberOfLines:
                print("WARN: More tests than specified: {0} instead of {1}".format(z, numberOfLines))

    z += 1


def calculate(initialStack, debug=False):
    # New algorithm because I jumped to a dumb conclusion last time
    flips = 0
    stack = list(initialStack)
    current = initialStack[0]
    if(debug):
        print("Flips is: {0}".format(flips))
        print("Stack is: {0}".format("".join(stack)))

    cursor = 1
    while cursor < len(initialStack):
        if stack[cursor] is not current:
            flips += 1
            current = stack[cursor]

            flipStack(stack, cursor)
            if(debug):
                print("Flips is: {0}".format(flips))
                print("Stack is: {0}".format("".join(stack)))
        cursor += 1

    sample = stack[0]
    if sample == '-':
        flips += 1
        flipStack(stack, cursor)
        if(debug):
            print("Flips is: {0}".format(flips))
            print("Stack is: {0}".format("".join(stack)))


    if debug:
        print("----------------")
    return flips

def flipStack(stack, numberToFlip):
    if(numberToFlip > len(stack)):
        print("WARN: Flipping too many, there's a bug")
        return

    temp = []
    # Index is excluded -- stack is number
    for i in stack[0: numberToFlip]:
        top = stack.pop(0)
        flip = flipPancake(top)
        temp.append(flip)

    for pc in temp:
        stack.insert(0, pc)

def flipPancake(pc):
    if pc == "-":
        return "+"
    if pc == "+":
        return "-"

def parseInput(inp):
    stack = []
    for char in inp:
        if char == '-' or char == '+':
            stack.append(char)
    return stack

outArray = []
i = 1
for test in data:
    testStack = parseInput(test)
    value = calculate(testStack,False)
    out = "Case #{0}: {1}".format(i, value)
    outArray.append(out)
    print(out)
    i += 1

with open('output.txt', 'w') as o:
    o.write('\n'.join(outArray))
