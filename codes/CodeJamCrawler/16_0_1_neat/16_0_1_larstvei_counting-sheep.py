from sys import stdin

for t in range(1, int(stdin.readline()) + 1):
    n = int(stdin.readline())

    if n == 0:
        print 'case #%d: insomnia' % t
        continue

    seen = set([])
    sleep = set('0123456789')
    i = 1

    while True:
        m = n * i
        seen |= set(str(m))
        if seen == sleep:
            print 'case #%d: %d' % (t, m)
            break
        i += 1
