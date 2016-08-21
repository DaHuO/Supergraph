from multiprocessing import Pool
from collections import defaultdict

def st(s):
    n = len(s)
    if (n > 1):
        l = st(s[:n/2])
        r = st(s[n/2:])
        if l > r:
            return r + l
        return l+r
    return s

def solve(line):
    n, r, p, s = map(int, line.strip().split())
    res = "IMPOSSIBLE"
    tr = "R"
    for i in xrange(n):
        rr = 0
        pp = 0
        ss = 0
        ttr = ""
        for j in xrange(len(tr)):
            if tr[j] == "R":
                rr += 1
                ss += 1
                ttr += "RS"
            if tr[j] == "S":
                ss += 1
                pp += 1
                ttr += "PS"
            if tr[j] == "P":
                pp += 1
                rr += 1
                ttr += "PR"
        tr = ttr
        if rr == r and pp ==p and ss == s:
            return st(tr)
    tr = "S"
    for i in xrange(n):
        rr = 0
        pp = 0
        ss = 0
        ttr = ""
        for j in xrange(len(tr)):
            if tr[j] == "R":
                rr += 1
                ss += 1
                ttr += "RS"
            if tr[j] == "S":
                ss += 1
                pp += 1
                ttr += "PS"
            if tr[j] == "P":
                pp += 1
                rr += 1
                ttr += "PR"
        tr = ttr
        if rr == r and pp == p and ss == s:
            return st(tr)
    tr = "P"
    for i in xrange(n):
        rr = 0
        pp = 0
        ss = 0
        ttr = ""
        for j in xrange(len(tr)):
            if tr[j] == "R":
                rr += 1
                ss += 1
                ttr += "RS"
            if tr[j] == "S":
                ss += 1
                pp += 1
                ttr += "PS"
            if tr[j] == "P":
                pp += 1
                rr += 1
                ttr += "PR"
        tr = ttr
        if rr == r and pp == p and ss == s:
            return st(tr)
    return res



p = Pool(8)
with open("in.txt", "r") as fin:
    results = p.map(solve, fin.readlines()[1:])
    with open("out.txt", "w") as fout:
        i = 0
        for res in results:
            i += 1
            fout.write("Case #%d: %s\n" % (i, str(res)))
