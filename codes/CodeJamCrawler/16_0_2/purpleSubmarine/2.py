t = int(raw_input())

for p in xrange(1, t + 1):
    s = raw_input()
    ans = 0
    for i in xrange(len(s) - 1, -1, -1):
        if (ans % 2 == 0):
            if s[i] == '-':
                ans += 1
        else:
            if s[i] == '+':
                ans += 1
    print "Case #{}: {}".format(p, ans)