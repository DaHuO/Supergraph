import sys
def output(stack):
    def flip(stack, i):
        top = stack[:i + 1]
        #print "top %s" % top
        bottom = stack[i + 1:]
        #print "bottom %s" % bottom
        new_stack = map(lambda x: not x, top[::-1]) + bottom
        assert len(stack) == len(new_stack)
        return new_stack

    flips = 0
    for i in range(len(stack) - 1, -1, -1):
        #print i, flips, stack
        if stack[i] == False:
            if stack[0]:
                top_flip = stack.index(False) - 1
                if top_flip >= 0:
                    stack = flip(stack, top_flip)
                    flips += 1
                    #print "meio", i, flips, stack
            stack = flip(stack, i)
            flips += 1
            #print "vira", i, flips, stack
    assert(all(stack))
    return flips

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        stack = map(lambda x: x == "+", sys.stdin.readline().strip())
        answer = output(stack)
        print "Case #%d: %s" % (t + 1, answer)
