tests = int(raw_input())


def reverse(stack, pos):
    return [i ^ 1 for i in reversed(stack[:pos + 1])] + stack[pos + 1:]

for test in xrange(1, tests + 1):
    stack = [0 if i == '-' else 1 for i in raw_input()]
    # print stack
    res = 0
    i = len(stack)
    while sum(stack) != len(stack):
        i -= 1
        if stack[i]:
            continue
        # print ">", i, stack
        if stack[0]:
            positive_index = 0
            while stack[positive_index + 1]:
                positive_index += 1
            # print "<<", stack[:positive_index + 1]
            stack = reverse(stack, positive_index)
            res += 1
        stack = reverse(stack, i)
        # print "<", i, stack
        res += 1
    print "Case #{}: {}".format(test, res)
