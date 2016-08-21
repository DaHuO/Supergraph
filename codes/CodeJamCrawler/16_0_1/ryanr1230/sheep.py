T = int(raw_input())
for i in range(T):
    orig_N = int(raw_input())
    if orig_N == 0:
        print "Case #%d: INSOMNIA" % (i + 1)
        continue
    seen = [False for x in range(10)]
    multiplier = 1
    N = orig_N
    while seen.count(False) > 0:
        N = orig_N * multiplier
        parse_N = N
        while parse_N > 0:
            seen[parse_N % 10] = True
            parse_N /= 10
        multiplier += 1
    print "Case #%d: %d" % ((i+1), N)
