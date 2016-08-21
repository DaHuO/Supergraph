_T = T = input()
while T > 0:
    T -= 1
    N = input()
    senators = map(int, raw_input().split())
    senators = zip(senators, range(len(senators)))
    total = 0
    res = list()
    for s, i in senators:
        total += s
    while total > 0:
        senators.sort(reverse=True)
        if total == 3:
            senators[0] = (senators[0][0] - 1, senators[0][1])
            total -= 1
            res.append((senators[0][1], -1))
        elif senators[0][0] == senators[1][0]:
            senators[0] = (senators[0][0] - 1, senators[0][1])
            senators[1] = (senators[1][0] - 1, senators[1][1])
            total -= 2
            res.append((senators[0][1], senators[1][1]))
        elif senators[0][0] > senators[1][0] + 1:
            senators[0] = (senators[0][0] - 2, senators[0][1])
            total -= 2
            res.append((senators[0][1], senators[0][1]))
        else:
            senators[0] = (senators[0][0] - 1, senators[0][1])
            total -= 1
            res.append((senators[0][1], -1))
    _ret = list()
    for r in res:
        if r[1] == -1:
            _ret.append(chr(ord('A') + r[0]))
        else:
            _ret.append(chr(ord('A') + r[0]) + chr(ord('A') + r[1]))
    print "Case #%d: " %(_T - T), ' '.join(_ret)
        
