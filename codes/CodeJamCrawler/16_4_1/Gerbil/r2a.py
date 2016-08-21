from collections import Counter

def result(input):
    N, R, P, S = map(int, input.split(' '))
    a, b, c = 'P', 'R', 'S'
    m = [(P, R, S)]
    t = [('P', 'R', 'S')]
    while N:
        N -= 1
        m.append(((P + R - S) // 2, (R + S - P) // 2, (P + S - R) // 2))
        t.append((min(a + b, b + a), min(b + c, c + b), min(a + c, c + a)))
        P, R, S = m[-1]
        a, b, c = t[-1]
        if any(x < 0 for x in m[-1]):
            return 'IMPOSSIBLE'
    return t[-1][m[-1].index(1)]



f = open('A-large.in')
r = f.readlines()
w = open('A-large.out','w')

i = 1
while i < len(r):
    w.write('Case #%d: %s\n' % (i, result(r[i].strip())))
    #print('Case #%d: %s\n' % (i, result(r[i].strip())))
    i += 1
f.close()
w.close()
