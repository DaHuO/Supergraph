l = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def f(s, n):
    if n == 10:
        if s == "":
            return ""
        else:
            return False
    else:
        poss_res = f(s, n+1)
        if poss_res != False:
            return poss_res
        w = l[n]
        count = len(w)
        for c in w:
            if s.count(c) >= w.count(c):
                count -= 1
        if count == 0:
            for c in w:
                s = s.replace(c, "", 1)
            if f(s, n) != False:
                return str(n) + f(s, n)
            else:
                return False
        else:
            return False

N = int(raw_input())
for i in xrange(N):
    s = raw_input()
    res = f(s, 0)
    print "Case #%d: %s" % (i+1, res)
