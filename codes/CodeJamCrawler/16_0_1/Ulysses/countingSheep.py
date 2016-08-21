
case = input()

def solve(n):
    visited = set()
    used = set([str(q) for q in xrange(10)]);
    k = 1
    while True:
        s = str(k * n)
        for c in s:
            if c in used:
                used.remove(c)
                if len(used) == 0:
                    return s
        if s in visited:
            return 'INSOMNIA'
        else:
            visited.add(s)
        k += 1


for i in xrange(1, case+1):
    print 'Case #%d: %s' % (i, solve(input()))
