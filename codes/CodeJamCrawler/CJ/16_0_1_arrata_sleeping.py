import sys

n = int(sys.stdin.readline())

for i in range(n):
    t = int(sys.stdin.readline())
    check = {}
    total = 10
    for x in range(10):
        check[x] = False
        total += x
    ret = 0
    if t == 0:
        ret = 'INSOMNIA'
    else:
        buf = t
        counter = 0
        while total:
            for x in str(buf):
                if not check[int(x)]:
                    total -= int(x)
                    if int(x) == 0:
                        total -= 10
                    check[int(x)] = True
            buf += t
            counter += 1
        ret = counter * t

    print "Case #%d:" % (i + 1), ret
