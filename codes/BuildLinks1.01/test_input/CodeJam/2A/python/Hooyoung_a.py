memo = {}

def solve(x,R,P,S):
    if (x,R,P,S) in memo:
        return memo[(x,R,P,S)]
    out = False
    if R + P + S == 1:
        if x == 0 and R == 1:
            out = 'R'
        elif x == 1 and P == 1:
            out = 'P'
        elif x == 2 and S == 1:
            out = 'S'
    else:
        n = (R + P + S) / 2

        for r in xrange(0,min(R,n)+1):
            for p in xrange(0,min(P,n-r)+1):
                s = n-r-p
                if s <= S:
                    a = solve(x,r,p,s)
                    b = solve((x+2)%3, R-r,P-p,S-s)
                    if a and b and ((not out) or a+b < out):
                        out = a+b
                    a = solve((x+2)%3,r,p,s)
                    b = solve(x, R-r,P-p,S-s)
                    if a and b and ((not out) or a+b < out):
                        out = a+b
    memo[(x,R,P,S)] = out
    return out
    
T = int(raw_input())
for t in xrange(1,T+1):
    N,R,P,S = map(int,raw_input().split())
    out = False
    for x in xrange(3):
        y = solve(x,R,P,S)
        if y and ((not out) or y < out):
            out = y
    print "Case #%d:" % t, out if out else "IMPOSSIBLE"
