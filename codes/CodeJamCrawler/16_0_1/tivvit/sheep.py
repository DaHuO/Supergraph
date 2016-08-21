tests = int(raw_input())

for test in xrange(1, tests + 1):
    n = int(raw_input())
    if n == 0:
        res = "INSOMNIA"
    else:
        cnts = {str(n): 0 for n in range(10)}
        i = 2
        res = n
        while True:
            digits = str(res)
            for d in digits:
                cnts[d] += 1

            # print j - 1, [(k,v) for k, v in sorted(cnts.items())]
            if len(filter(lambda x: x < 1, cnts.values())) == 0:
                break

            res = n * i
            i += 1

    print "Case #{}: {}".format(test, res)
