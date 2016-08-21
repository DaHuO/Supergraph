def getRes(s):
    f = [0]
    g = [0]
    l = len(s)
    for i in range(0, l):
        if s[i] == '-':
            f.append(min(g[i]+1,f[i]+2))
            g.append(min(g[i],f[i]+1))
        else:
            f.append(min(g[i]+1,f[i]))
            g.append(min(g[i]+2,f[i]+1))
    return f[l]

t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    print("Case #{idx}: {res}".format(idx=i, res=getRes(s)))
