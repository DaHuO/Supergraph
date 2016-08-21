def solve(n):
    if 0 == n:
        return "INSOMNIA"
    i, s, numbers = 1, set(), set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    while s != numbers:
        s |= set(list(str(i * n)))
        i += 1
    return n * (i - 1)


for t in xrange(int(input())):
    print "Case #" + str(t+1) + ": " + str(solve(int(input())))
