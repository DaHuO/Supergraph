## Problem B

def probB(stack, target):
    if len(stack) == 1:
        return 0 if stack == target else 1
    if stack[-1] == target:
        return probB(stack[:-1], target)
    else:
        return probB(stack[:-1], stack[-1]) + 1
    
for i in range(1, int(raw_input()) + 1):
    print "Case #%d: %s" % (i, probB(raw_input(), '+'))
