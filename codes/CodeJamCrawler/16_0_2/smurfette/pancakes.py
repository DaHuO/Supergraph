def is_stack_ok(stack):
    for c in stack:
        if c == '-':
            return False
    return True

def invalid(stack):
    index = len(stack)
    for c in stack[::-1]:
        if c == '-':
            return stack[0:index]
        index -= 1
    return []
            
def min_flips(stack):
    if len(stack) == 0:
        return 0
    flip = 0
    for i in range(len(stack)-1):
        if stack[i]!=stack[i+1]:
            flip += 1
    return flip + 1

        

t = int(raw_input())
for i in xrange(1, t + 1):
    stack = [s for s in raw_input()]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, min_flips(invalid(stack)))
