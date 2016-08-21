import sys
import string

# Arguments: [in] [out]
# Defaults: in='input.txt', out=stdout

def appok(r, rs, cs):
    i = len(rs)
    rs.append(r)
    ok = True
    for j in xrange(len(cs)):
        if len(cs[j]) > i and len(rs[i]) > j:
            ok = ok and cs[j][i] == rs[i][j]
    if not ok:
        del rs[i]
    return ok

# Returns list of commands
def findnext(m, i, rs, cs, w):
    # Did we finish?
    if i==len(m) and w==True:
        return (rs,cs)
    if i<len(m):
        # Try as a row
        if len(rs) < N and appok(m[i], rs, cs):
            res = findnext(m,i+1,rs,cs,w)
            if res != 0: return res
            del rs[-1]
        # Try as a col
        if len(cs) < N and appok(m[i], cs, rs):
            res = findnext(m,i+1,rs,cs,w)
            if res != 0: return res
            del cs[-1]
    # Try as a wildcard
    if not w and len(rs) < N:
        rs.append([])
        res = findnext(m,i,rs,cs,True)
        if res != 0: return res
        del rs[-1]
    # Give up
    return 0

if len(sys.argv) > 1:
    input_file = len(sys.argv)>1 and sys.argv[1] or 'input.txt'
    outf = len(sys.argv)>2 and open(sys.argv[2],'w') or sys.stdout
    with open(input_file) as f:
        T = int(f.readline())
        for x in range(T):
            N = map(int, f.readline().split(' '))[0]
            m = []
            for n in xrange(2*N-1):
                vs = map(int, f.readline().split(' '))
                m.append(vs)
            m.sort()
            # Define it to be a missing row
            rs = []
            cs = []
            sol = findnext(m, 0, rs, cs, False)
            assert(sol != 0)
            print sol
            # Find wildcard row
            r = sol[0].index([])
            mr = [sol[1][c][r] for c in xrange(len(cs))]
            outf.write('Case #{0}: '.format(x+1))
            outf.write(' '.join(map(str,mr)))
            outf.write('\n')
