t = input()


def calNum(n):
    if n == 0:
        return "INSOMNIA"
    a = set(str(n))
    count = len(a)
    i = 2
    while True:
        a = a.union(set(str(n * i)))
        if len(a) == 10:
            break
        i += 1
    return n * i

i = 1
while t:
    t -=1
    n = input()
    print "Case #" + str(i) + ": " + str(calNum(n))
    i += 1