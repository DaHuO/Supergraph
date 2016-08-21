num = input()

for i in xrange(num):
    n = raw_input()
    f = '-'
    tot = 0
    for c in n[::-1]:
        if c == f:
            tot += 1
            if f == '-':
                f = '+'
            else:
                f = '-'
    print 'Case #%i:' % (i+1),  tot


