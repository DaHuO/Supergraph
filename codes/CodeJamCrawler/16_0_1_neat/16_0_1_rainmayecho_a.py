
def g(n):
    seen = set([int(e) for e in str(n)])
    if not n:
        return 'INSOMNIA'
    i = 1
    while True:
        x = n*i
        for d in str(x):
            seen.add(int(d))
        if len(seen) == 10:
            return x
        i += 1
    return x

h = open('1aout.txt', 'w')

f1 = 'test.txt'
f2 = '1alarge.in'

with open(f2, 'r') as f:
    T = f.readline()
    for i, e in enumerate(f.readlines()):
        n = int(e)
        result = g(n)
        print 'Case #%s: %s' %(i + 1, result)
        h.write('Case #%s: %s\n' %(i + 1, result))
