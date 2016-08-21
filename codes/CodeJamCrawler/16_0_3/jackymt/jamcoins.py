def factor(n):
    x = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i

def solution(n, j):
    rs = []
    for i in xrange(1, ((2 ** n) + 1)):
        b = ('{0:0%sb}' % n).format(i)
        assert (i == int(b, 2))
        
        if b.startswith('0') or b.endswith('0'):
            continue

        bases = [int(b, x) for x in xrange(2, 11)]
        factors = map(factor, bases)
        v_factors = filter(lambda x: x is not None, factors)

        if len(v_factors) != len(bases):
            continue

        rs.append((b, factors))

        if len(rs) == j:
            break

    return rs

with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        if i > 0:
            line = line.strip('\n')
            n, j = line.split()
            x = solution(int(n), int(j))
            
            print "Case #{}:".format(i)
            for e in x:
                print e[0], ' '.join(map(str, e[1]))