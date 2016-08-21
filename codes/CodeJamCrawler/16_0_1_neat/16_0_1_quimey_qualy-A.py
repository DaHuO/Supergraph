T = input()
for t in range(T):
    N = input()
    i = 1
    d = set()
    while N and len(d) < 10:
        d.update(str(i * N))
        i += 1
    ans = str((i - 1) * N) if N else "INSOMNIA"
    print "Case #%d: %s" % (t + 1, ans)
