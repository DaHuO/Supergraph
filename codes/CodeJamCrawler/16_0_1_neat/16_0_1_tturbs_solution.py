_T = T = input()
while T > 0:
    T -= 1
    N = input()
    if N == 0:
        print "Case #%d: INSOMNIA" % (_T - T)
        continue
    mask = 0
    i = 0
    while mask != 1023:
        i += 1
        divN = N * i
        while divN > 0:
            restN = divN % 10
            divN /= 10
            mask |= 1 << restN
    print "Case #%d:" % (_T - T), N * i
