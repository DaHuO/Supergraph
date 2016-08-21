
def rec(s1, pre1, s2, pre2):
    if len(s1) == 0:
        return (abs(pre1 - pre2), pre1, pre2)
    if s1[0] != '?' and s2[0] != '?':
        pre1 = pre1 * 10 + int(s1[0])
        pre2 = pre2 * 10 + int(s2[0])
        return rec(s1[1:], pre1, s2[1:], pre2)
    if s1[0] == '?' and s2[0] == '?':
        if pre1 == pre2:
            res = rec(s1[1:], pre1 * 10, s2[1:], pre2 * 10)
            res = min(res, rec(s1[1:], pre1 * 10, s2[1:], pre2 * 10 + 1))
            res = min(res, rec(s1[1:], pre1 * 10 + 1, s2[1:], pre2 * 10))
            return res
        elif pre1 < pre2:
            return rec(s1[1:], pre1 * 10 + 9, s2[1:], pre2 * 10)
        else:
            return rec(s1[1:], pre1 * 10, s2[1:], pre2 * 10 + 9)
    if s1[0] == '?':
        if pre1 == pre2:
            res = rec(s1[1:], pre1 * 10 + int(s2[0]), s2[1:], pre2 * 10 + int(s2[0]))
            if int(s2[0]) > 0:
                res = min(res, rec(s1[1:], pre1 * 10 + int(s2[0]) - 1, s2[1:], pre2 * 10 + int(s2[0])))
            if int(s2[0]) < 9:
                res = min(res, rec(s1[1:], pre1 * 10 + int(s2[0]) + 1, s2[1:], pre2 * 10 + int(s2[0])))
            return res
        elif pre1 < pre2:
            return rec(s1[1:], pre1 * 10 + 9, s2[1:], pre2 * 10 + int(s2[0]))
        else:
            return rec(s1[1:], pre1 * 10, s2[1:], pre2 * 10 + int(s2[0]))
    if s2[0] == '?':
        if pre1 == pre2:
            res = rec(s1[1:], pre1 * 10 + int(s1[0]), s2[1:], pre2 * 10 + int(s1[0]))
            if int(s1[0]) > 0:
                res = min(res, rec(s1[1:], pre1 * 10 + int(s1[0]), s2[1:], pre2 * 10 + int(s1[0]) - 1))
            if int(s1[0]) < 9:
                res = min(res, rec(s1[1:], pre1 * 10 + int(s1[0]), s2[1:], pre2 * 10 + int(s1[0]) + 1))
            return res
        elif pre1 < pre2:
            return rec(s1[1:], pre1 * 10 + int(s1[0]), s2[1:], pre2 * 10)
        else:
            return rec(s1[1:], pre1 * 10 + int(s1[0]), s2[1:], pre2 * 10 + 9)


def run():
    s1, _, s2 = input().strip().partition(' ')
    res = rec(s1, 0, s2, 0)
    return (("%%0%dd" % len(s1)) % res[1]), (("%%0%dd" % len(s2)) % res[2])


t = int(input().strip())
for i in range(t):
    res = run()
    print("Case #%d: %s %s" % (i+1, res[0], res[1]))

