MAX = 10**5
for i in xrange(int(raw_input())):
    N = int(raw_input())
    s = "INSOMNIA"
    if N != 0:
        count = 10
        seen = {}
        for c in "0123456789":
            seen[c] = False
        n = N
        done = False
        for _ in xrange(MAX):
            for c in str(n):
                if not seen[c]:
                    seen[c] = True
                    count -= 1
                    if count == 0:
                        s = str(n)
                        break
            if s != "INSOMNIA":
                break
            n += N
    print "Case #%d: %s" % (i+1, s)
