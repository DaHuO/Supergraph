t = int(raw_input())
for index in xrange(1, t+1):
    n = int(raw_input())
    if n == 0:
        print 'Case #{}: {}'.format(index, 'INSOMNIA')
    else:
        res = set()
        i = 0
        while len(res) < 10:
            i += 1
            res = res | set(list(str(i*n)))
        print 'Case #{}: {}'.format(index, i*n)
