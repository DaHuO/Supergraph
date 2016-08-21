from sys import argv
lines = open(argv[1]).readlines()
numcases = int(lines[0])


def solve_stack(stack, target=True):
    if stack==[target] or stack ==[]:
        return 0
    if stack[-1]==target:
        return solve_stack(stack[:-1], target)
    else:
        return 1 + solve_stack(stack[:-1], not target)

def read_stack(stack):
    return [s=='+' for s in stack if s in ('-', '+')]

for i, stack in enumerate(lines[1:]):
    casenum = i+1
    flips = solve_stack(read_stack(stack), True)
    print 'Case #%d: %d' % (casenum, flips)
