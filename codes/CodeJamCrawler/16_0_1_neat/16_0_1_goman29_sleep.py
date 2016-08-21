t = raw_input()


def sleep(n):
    if n ==0 :
        return "INSOMNIA"
    i = 0
    arr = [0] * 10
    while True:
        i += 1
        t = i*n
        for idx,char in enumerate(str(t)):
            arr[int(char)] = 1
        sum = 0
        for x in arr:
            sum+=x
        if sum == 10:
            return i * n

for x in xrange(int(t)):
    print "Case #%s: %s" % (x+1, sleep(int(raw_input())))

