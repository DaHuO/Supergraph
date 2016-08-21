T = input()
for t in range(T):
    N = input()
    seen = set()
    if N == 0:
        print "Case #%d: INSOMNIA" % (t + 1)
        continue
    i = 1
    while(len(seen) != 10):
        new = str(N * i)
        seen.update(new)
        i+=1
    print "Case #%d: %d" % (t + 1, N * (i - 1))
