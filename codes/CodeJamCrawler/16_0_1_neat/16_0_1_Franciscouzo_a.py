cases = int(raw_input())
for case in xrange(1, cases + 1):
    start = int(raw_input())
    seen = set()
    for i in xrange(1, 100001):
        n = i * start
        seen.update(set(str(n)))
        if len(seen) == 10:
            print 'Case #{}: {}'.format(case, n)
            break
    else:
        print 'Case #{}: INSOMNIA'.format(case)
