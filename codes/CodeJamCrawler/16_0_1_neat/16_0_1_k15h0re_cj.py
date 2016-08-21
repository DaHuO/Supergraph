cases = int(raw_input())
for i in xrange(cases):
    digits = list("1234567890")
    inp = int(raw_input())
    if inp == 0:
        ret = "INSOMNIA"
    else:
        for j in xrange(1, 10000000000000):
            a = str(inp * j)
            [digits.remove(x) for x in a if x in digits]
            if len(digits) == 0:
                ret = a
                break
    print "Case #{}: {}".format(i + 1, ret)
