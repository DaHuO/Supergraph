from itertools import product

def f(s1, s2):
    n = len(s1)
    l = []
    for i in product(range(10), repeat=s1.count("?")+s2.count("?")):
        x, y = s1, s2
        for d in i:
            if "?" in x:
                x = x.replace("?", str(d), 1)
            else:
                y = y.replace("?", str(d), 1)
        l.append((int(x), int(y)))
    min_dist = min(abs(i[0] - i[1]) for i in l)
    new_l = [i for i in l if abs(i[0]-i[1]) == min_dist]
    res = sorted(new_l)[0]
    res1, res2 = res
    res1 = str(res1)
    res2 = str(res2)
    while len(res1) < n:
        res1 = "0" + res1
    while len(res2) < n:
        res2 = "0" + res2
    return res1, res2

for i in xrange(int(raw_input())):
    in1, in2 = raw_input().split()
    r1, r2 = f(in1, in2)
    print "Case #%d: %s %s" % (i+1, r1, r2)
