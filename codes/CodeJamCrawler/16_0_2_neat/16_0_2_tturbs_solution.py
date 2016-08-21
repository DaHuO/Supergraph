_T = T = input()
while T > 0:
    T -= 1
    cake = raw_input()
    c = map(lambda s: s == '-' and 1 or 0, cake)
    res = 0
    for i in range(len(c) - 1, -1, -1):
        if c[i] == 1:
            res += 1
            for j in range(i + 1):
                c[j] = (c[j] + 1) % 2
    print "Case #%d:" % (_T - T), res
