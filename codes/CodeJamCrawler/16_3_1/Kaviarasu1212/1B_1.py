from collections import OrderedDict

t = int(raw_input())  # read a line with a single integer

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for z in xrange(1, t + 1):
    dic = {}
    def add(m, n):
        dic[m] = int(n)
    parties = raw_input()
    lines = (raw_input()).split()
    tmp = {add(s, l) for l, s in zip(lines, string) if l}
    dic = OrderedDict(sorted(dic.items(), key=lambda t: t[1], reverse=True))
    ans = ""
    while any(dic.values()):
        i, j = list(dic.items())[:2]
        k1, i = i
        k2, j = j
        k = i - j
        if k == 0:
            l = list(dic.items())[2:3]
            if l and i == j == l[0][1]:
                dic[k1] -= 1
                ans += " %s" % (k1)
            else:
                dic[k1] -= 1
                dic[k2] -= 1
                ans += " %s%s" %(k1, k2)
        elif k == 1:
            if i > 1:
                dic[k1] -= 2
                ans += " %s%s" % (k1, k1)
            else:
                dic[k1] -= 1
                ans += " %s" % (k1)
        else:
            dic[k1] -= 2
            ans += " %s%s" % (k1, k1)
        dic = OrderedDict(sorted(dic.items(), key=lambda t: t[1], reverse=True))

    print "Case #{}: {}".format(z, ans)
