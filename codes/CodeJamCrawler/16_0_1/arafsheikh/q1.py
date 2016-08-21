t = int(raw_input())

def _has(seen):
    for x in xrange(10):
        if x not in seen:
            return False
    return True

for x in xrange(t):
    seen = []
    n = int(raw_input())
    mul = -1
    for y in xrange(1, 101):
        mul = y*n
        seen += map(int, list(str(mul)))
        seen = list(set(seen))
        if (_has(seen)):
            print "Case #%i:"%(x+1), mul
            break
    else:
        print "Case #%i: INSOMNIA"%(x+1)

