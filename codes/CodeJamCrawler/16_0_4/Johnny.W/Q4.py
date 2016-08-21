def solve(k,c,s):
    if s == k:
        return " ".join(str(x) for x in xrange(1, s + 1))
    return 'not done:)'

T = input()
for c in xrange(1, T + 1):
    K,C,S = [int(k) for k in raw_input().split()]
    # print K,C,S
    res = solve(K,C,S)
    print "Case #%d: %s"%(c,res)