t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    k, c, s = s.split(' ')
    s = int(s)
    res = ' '.join([str(x) for x in range(1, s+1)])
    print("Case #{idx}: {seq}".format(idx=i, seq=res))
