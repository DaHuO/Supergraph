test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    n = int(raw_input())
    l = [int(i) for i in raw_input().split()]

    r = []
    m = {}
    for i in xrange(n):
        r.append([chr(ord('A') + i), l[i]])
    res = ''

    r.sort(key=lambda x: x[1], reverse=True)
    while r[0][1] != 0:
        #print r
        if r[0][1] > r[1][1] + 2:
            res += str(r[0][0])
            res += str(r[0][0])
            res += ' '
            r[0][1] -= 2
        elif r[0][1] > r[1][1] + 1 and r[1][1] != 0:
            res += r[0][0]
            res += r[1][0]
            res += ' '
            r[0][1] -= 1
            r[1][1] -= 1
        elif r[0][1] > r[1][1] + 1:
            res += r[0][0]
            res += ' '
            r[0][1] -= 1
        else:
            if len(r) > 2 and r[2][1] == r[0][1] == 1:
                res += str(r[0][0])
                r[0][1] -= 1
                res += ' '
            else:
                res += str(r[0][0])
                res += str(r[1][0])
                res += ' '
                r[0][1] -= 1
                r[1][1] -= 1
        r.sort(key=lambda x: x[1], reverse=True)
    #print res

    print "Case #{}: {}".format(case, res.strip())