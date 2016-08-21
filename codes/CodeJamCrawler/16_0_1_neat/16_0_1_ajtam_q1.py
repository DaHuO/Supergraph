f = open('q1.txt', 'r')
i = 0

for s in f:
    if i == 0:
        i = i + 1
        case = s
        continue
    if i > int(case):
        break
    value = int(s)
    if value == 0:
        print "Case #%d: INSOMNIA" % i
        i += 1
        continue
    v = range(0, 10)
    j = 0
    while len(v) > 0:
        j += 1
        k = value*j
        for x in str(k):
            if int(x) in v:
                v.remove(int(x))

    print "Case #%d: %s" % (i, k)
    i = i + 1

f.close()
