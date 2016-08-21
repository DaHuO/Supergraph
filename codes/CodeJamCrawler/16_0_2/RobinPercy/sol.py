T = int(raw_input())

def flip(stack, bot, top):

    for i in xrange((top - bot)/2 + 1):
        #print "swap %d and %d" % (bot+i, top-i)
        tmp = stack[bot+i]
        stack[bot+i] = not stack[top-i]
        stack[top-i] = not tmp


def fixbot(stack, bot, top):
    if not stack[-1]:
        flip(stack, bot, top)
        return 1

    nextTrue = None
    for i in xrange(bot, top + 1):
        if stack[i]:
            nextTrue = i
            break

    if nextTrue == None:
        flip(stack, bot, top)
        return 1

    #print "flip1: %d, %d, %d" % (bot, nextTrue, top)
    flip(stack, nextTrue, top)
    #print stack
    #print "flip2: %d, %d" % (bot, top)
    flip(stack, bot, top)
    return 2

def solve(t):
    stack = [x == '+' for x in reversed(raw_input())]
    flips = 0
    top = len(stack) - 1
    bot = 0
    #print stack

    for i in xrange(top+1):
        if stack[i]:
            bot += 1
            continue
        else:
            flips += fixbot(stack, i, top)
    #        print stack

    print "Case #%d: %d" % (t, flips)
    #print ""


for t in xrange(1, T+1):
    solve(t)
