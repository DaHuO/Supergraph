t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())

    if n == 0:
        print "Case #{}: {}".format(i, "INSOMNIA")
    else:
        j = 1
        counter = set(str(n))
        while len(counter) != 10:
            j += 1
            res = n * j
            counter.update(list(str(res)))
        print "Case #{}: {}".format(i, res)

