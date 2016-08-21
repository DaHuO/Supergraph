t = int(raw_input())
for i in xrange(1, t + 1):
    digits_seen = [False] * 10
    n = int(raw_input())
    if n == 0:
        print "Case #{}: INSOMNIA".format(i)
    else:
        res = 0
        while not all(digits_seen):
            res += n
            digits = str(res)
            for d in digits:
                digits_seen[int(d)] = True
        print "Case #{}: {}".format(i, res)
