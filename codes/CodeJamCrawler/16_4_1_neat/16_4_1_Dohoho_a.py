import itertools

n = int(raw_input())

def red(x):
    i = 0
    r = ''
    if len(x) == 1:
        #print 'ok'
        return True
   # print x
    while len(x[i:i+2]) != 0:
        xx = ''.join(sorted(x[i:i+2]))
       # print xx
        i += 2
        if xx == 'PR':
            r += 'P'
        elif xx == 'PS':
            r += 'S'
        elif xx == 'RS':
            r += 'R'
        else:
            #print 'no',len(xx),xx
            return False
    return red(r)

for nn in xrange(n):
    [i, r, p, s] = map(int, raw_input().split())
    res = 'IMPOSSIBLE'
    s = 'R'*r + 'P'*p + 'S'*s
    for x in itertools.permutations(s):
        #x = ''.join(x)
        if red(x) and (''.join(x) < res or res == 'IMPOSSIBLE'):
            #print 'wtf'
            res = ''.join(x)
    print "Case #{}: {}".format(nn+1, res)