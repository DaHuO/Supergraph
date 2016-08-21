def doit(stack):
    res = 0
    previous = stack[0]
    for c in stack:
        if c != previous:
            res += 1
            previous = c
    if stack[-1] == "-":
        res += 1
    return res

nb_tests = int(raw_input())
for i in xrange(nb_tests):
    line = raw_input()
    res = doit(line)
    print "Case #%d: %s" % (i + 1, res)
