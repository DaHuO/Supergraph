def mmm(x):
    if (x == 0):
        return 1
    ret = 0
    while (x > 0):
        ret = ret | (1 << (x % 10))
        x = x / 10
    return ret


def calc(cnt):
    msk = 0
    x = input()
    for i in range(100):
        msk = msk | mmm(x * (i + 1))
        if (msk == 1023):
            print "Case #%d: %d" % (cnt, x * (i + 1))
            return
    print "Case #%d: INSOMNIA" % cnt


n = input()
for i in range(n):
    calc(i + 1)
