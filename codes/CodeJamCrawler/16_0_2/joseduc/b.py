def solve(s):
    flip_count = 0
    for i in xrange(len(s) - 1, -1, -1):
        c = s[i]
        if ((c == '-' and flip_count % 2 == 0) or
            (c == '+' and flip_count % 2 == 1)):
            flip_count += 1
    return flip_count


t = int(raw_input())

for i in xrange(t):
    c = solve(raw_input())
    print "Case #%s: %s" % ((i + 1), c)
