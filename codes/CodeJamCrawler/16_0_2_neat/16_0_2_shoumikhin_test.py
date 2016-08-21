def solve(s):
    p, r = s[0], 0
    for c in s[1:]:
        if p != c:
            p = c
            r += 1
    if s[-1] == '-':
        r += 1
    return r


for t in xrange(int(input())):
    print "Case #" + str(t+1) + ": " + str(solve(str(raw_input())))
