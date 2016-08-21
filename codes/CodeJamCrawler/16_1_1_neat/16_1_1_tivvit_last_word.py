tests = int(raw_input())

for test in xrange(1, tests + 1):
    n = raw_input()
    buff = ''
    res = ""
    for i in n:
        if i < buff:
            res += i
        else:
            res = i + res
            buff = i

    print "Case #{}: {}".format(test, res)
