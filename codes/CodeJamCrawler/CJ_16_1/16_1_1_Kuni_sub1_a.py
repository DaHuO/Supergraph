#coding: utf-8

def proc():
    s = raw_input()
    ret = s[0]
    for i in xrange(1, len(s)):
        if ret[0] <= s[i]:
            ret = s[i]+ret
        else:
            ret = ret + s[i]
    return ret

T = int(raw_input())
for t in xrange(T):
    print "Case #{}: {}".format(t+1, proc())
