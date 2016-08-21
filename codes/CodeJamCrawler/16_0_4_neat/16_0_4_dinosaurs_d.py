# SMALL
n = input()
for i in range(n):
    k, c, s = map(int, raw_input().split(' '))
    print 'Case #%d: %s' % (i + 1, ' '.join([str(1 + ss * k**(c-1)) for ss in range(s)]))
