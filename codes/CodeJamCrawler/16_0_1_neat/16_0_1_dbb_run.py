import sys

nlines = int(sys.stdin.readline())
casen = 0
while 1:
    line = sys.stdin.readline()
    casen += 1
    if not line:
        break
    n = int(line)
    if n == 0:
        print 'Case #%d: INSOMNIA' % casen  
        continue
    s = set()
    orig = n
    while 1:
        for c in str(n):
            s.add(c)
        if len(s) == 10:
            break
        n += orig
    print 'Case #%d: %d' % (casen, n)
