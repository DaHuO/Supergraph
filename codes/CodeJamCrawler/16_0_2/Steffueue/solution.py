def flip(stack, position, side, replacement):
    if position == -1:
        newstack = stack.replace(side, replacement)
    else:
        newstack = stack[0:position].replace(side, replacement) + stack[position:]
#    print "newstack: %s" % newstack
    return newstack

def getOpposite(side):
    if side == '+':
        return '-'
    else:
        return '+'

def solve(stack, flips):
    if '-' not in stack:
        return flips;
    else:
        side = stack[0]
        otherSide = getOpposite(side)
        posFlip = stack.find(otherSide);
        stack = flip(stack, posFlip, side, otherSide)
        flips += 1
        return solve(stack, flips)

def main():
    testcases = int(raw_input()) 
    for case in xrange(1, testcases + 1):
        stack = raw_input()
        print "Case #%d: %s" % (case, solve(stack, 0))

if __name__ == "__main__":
    main()
