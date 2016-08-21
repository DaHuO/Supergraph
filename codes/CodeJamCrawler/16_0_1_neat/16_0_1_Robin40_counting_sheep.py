def f(n):
    ans = 0
    seen = 0
    steps = 0
    while seen != 1023:
        ans += n
        s = str(ans)
        for c in s:
            d = ord(c)-48
            seen |= 1<<d
        steps += 1
    return (ans, steps)


T = input()
for t in xrange(1,T+1):
    n = input()
    print "Case #" + str(t) + ": " + ("INSOMNIA" if n == 0 else str(f(n)[0]))
