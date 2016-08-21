def solve(n):
    D = {}
    dn = n
    while True:
        digits = str(n)
        for d in digits:
            D.update({d:0})
        if len(D) == 10:
            return n
        n = n + dn

n = int(raw_input())
for i in range(n):
    x = int(raw_input())
    if x == 0:
        print 'Case #%d: INSOMNIA' % (i+1)
    else:
        print 'Case #%d: %d' % (i+1, solve(x))