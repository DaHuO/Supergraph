import sys

f = open(sys.argv[1])
o = open('a.txt', 'w')

tests = int(f.readline())

for step in range(1, tests + 1):
    n = int(f.readline())
    s = set()
    found = False

    for next in range(1, 100):
        _n = n * next
        s = s.union([int(i) for i in str(_n)])
        if (len(s) == 10):
            o.write('Case #%s: %s\n' % (step, _n))
            found = True
            break

    if not found:
        o.write('Case #%s: %s\n' % (step, 'INSOMNIA'))


o.flush()
o.close()
f.close()
