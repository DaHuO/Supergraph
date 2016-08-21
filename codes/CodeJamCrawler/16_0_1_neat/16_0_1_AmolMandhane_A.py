num_cases = input()

for T in xrange(num_cases):
    number = input()
    if number == 0:
        out = "INSOMNIA"
    else:
        d = {n: False for n in xrange(10)}
        mul = 1
        while True:
            digits = map(int, list(str(number * mul)))
            for dig in digits:
                d[dig] = True
            fl = True
            for dig in xrange(10):
                if not d[dig]:
                    mul += 1
                    fl = False
                    break
            if not fl:
                continue
            out = str(number * mul)
            break
    print "Case #%d: %s" % (T + 1, out)
