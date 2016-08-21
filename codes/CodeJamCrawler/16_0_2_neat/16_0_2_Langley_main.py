import sys
from sets import Set

def flip(stack, index):
    new_stack = []

    for idx in range(index, len(stack)):
        if stack[idx] == '+':
            new_stack.append('-')
        else:
            new_stack.append('+')
    return stack[0:index] + new_stack

def stack_happy(stack):
    stack = Set(stack)

    if len(stack) == 1 and '+' in stack:
        return True
    else:
        return False

def calculate(stack):
    stack = list(stack[::-1])

    if stack_happy(stack): return 0

    flips = 0
    for x in range(len(stack)):
        if stack_happy(stack): return flips
        if stack[x] == '+': continue
        stack = flip(stack, x)
        flips += 1

    return flips

def go():
    filename = sys.argv[1]

    with open(filename) as f:
        t = int(f.readline().strip())

        for x in range(1, t+1):
            value = f.readline().strip()
            print 'Case #%d: %s' % (x, calculate(value))

go()
