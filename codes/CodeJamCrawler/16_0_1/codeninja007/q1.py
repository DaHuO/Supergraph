def addDigit(d, lst):
    if d not in lst:
        lst.append(d)
    return lst


def foo(num, lst):
    digits = [int(x) for x in str(num)]
    for d in digits:
        lst = addDigit(d, lst)

    flag = False
    if len(lst) == 10:
        flag = True
        return (flag, num)
    else:
        for i in range(1, 1000000):
            n = i * num
            digits = [int(x) for x in str(n)]
            for d in digits:
                lst = addDigit(d, lst)
            if len(lst) == 10:
                flag = True
                break
    return (flag, n)


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    (sleep, num) = foo(n, [])
    if sleep:
        s = num
    else:
        s = "INSOMNIA"
    print "Case #{}: {}".format(i, s)
