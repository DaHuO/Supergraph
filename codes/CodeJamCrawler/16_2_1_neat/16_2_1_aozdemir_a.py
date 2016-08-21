import fileinput

c = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

T = 0
first = True
for line in fileinput.input():
    if first:
        first = not first
        continue
    T += 1
    line = line.strip()
    m = {}
    for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        m[l] = 0
    for cc in line:
        m[cc] += 1
    C = [0 for i in xrange(10)]
    C[0] = m['Z']
    for l in c[0]: m[l] -= C[0]
    #print C[0], c[0], m
    C[2] = m['W']
    for l in c[2]: m[l] -= C[2]
    #print C[2], c[2], m
    C[8] = m['G']
    for l in c[8]: m[l] -= C[8]
    #print C[8], c[8], m
    C[6] = m['X']
    for l in c[6]: m[l] -= C[6]
    #print C[6], c[6], m
    C[7] = m['S']
    for l in c[7]: m[l] -= C[7]
    #print C[7], c[7], m
    C[5] = m['V']
    for l in c[5]: m[l] -= C[5]
    #print C[5], c[5], m
    C[4] = m['F']
    for l in c[4]: m[l] -= C[4]
    #print C[4], c[4], m
    C[3] = m['T']
    for l in c[3]: m[l] -= C[3]
    #print C[3], c[3], m
    C[9] = m['I']
    for l in c[9]: m[l] -= C[9]
    #print C[1], c[1], m
    C[1] = m['O']
    for l in c[1]: m[l] -= C[1]
    for l in m:
        assert m[l] == 0, "ERR %s, %s\n%s" % (m, (l, m[l]), (C, line))
    out = ''
    for i in range(10):
        out += str(i) * C[i]
    print "Case #%d: %s" % (T,out)


