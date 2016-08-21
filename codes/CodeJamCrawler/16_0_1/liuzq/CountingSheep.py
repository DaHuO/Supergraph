T = input()

def lastNumber(num):
    if num == 0:
        return "INSOMNIA"
    mark = [0] * 10
    n = 1
    while True:
        N = num * n
        tmp = N
        while tmp:
            mark[tmp % 10] = 1
            tmp /= 10
        print N
        if sum(mark) == 10:
            return str(N)

        n += 1

for i in range(1,T + 1):
    N = input()
    print "Case #%d: %s" % (i, lastNumber(N))