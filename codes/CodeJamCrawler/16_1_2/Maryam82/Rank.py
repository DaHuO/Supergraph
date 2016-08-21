from collections import Counter;

inF = open('B-large.in-2.txt','r')
ouF = open('MaryamQBL.out','w')
t = int(inF.readline())
for n in xrange(t):
    s = int(inF.readline())
    o = []
    for i in xrange(2 * s - 1):
        o += inF.readline().strip().split()
    l = Counter(o)
    res = []
    for e in l:
        if l[e] % 2 != 0:
            res.append(int(e))
    Res = '';
    for e in sorted(res):
        Res = Res + ' ' + str(e)
    ouF.write('Case #' + str(n + 1) + ':' + Res+'\n')
