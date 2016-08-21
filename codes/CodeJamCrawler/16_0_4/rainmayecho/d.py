
def g(k, c, s):
    if k == 1:
        return 1
    if c == 1:
        if s < k:
            return 'IMPOSSIBLE'
        return ' '.join([str(i) for i in xrange(1, k+1)])

    if s < k/c:
        return 'IMPOSSIBLE'

    return ' '.join([str(i) for i in xrange(2, 1+s)])


h = open('1dout.txt', 'w')

f1 = 'dtest.txt'
f2 = '1dsmall.in'

with open(f2, 'r') as f:
    T = f.readline()
    for i, e in enumerate(f.readlines()):
        k, c, s = (int(x) for x in e.split())
        result = g(k, c, s)
        print 'Case #%s: %s' %(i + 1, result)
        h.write('Case #%s: %s\n' %(i + 1, result))
