import sys

fi = open('A-large.in', 'r')
fo = open('a.out', 'w')

T = int(fi.readline())
    
for t in xrange(T):
    # solve
    N = int(fi.readline())
    
    answer = ''
    if N == 0:
        answer = 'INSOMNIA'
    else:
        n = 1
        digits = 0
        while digits != 1023:
            check = N * n
            for d in str(check):
                digits |= (1 << (ord(d) - 48))
            n += 1
        answer = str((n - 1) * N)
    
    fo.write('Case #{}: {}\n'.format(t + 1, answer))
    print 'Case #{}: {}'.format(t + 1, answer)
    
fi.close()
fo.close()