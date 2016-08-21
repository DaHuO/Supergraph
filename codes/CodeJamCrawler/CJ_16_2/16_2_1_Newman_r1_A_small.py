#Rayun Mehrab - Round 1 Problem A Small

t = int(raw_input())

for i in xrange(1, t + 1):
    n = raw_input()
    d = {'z':0, 'n':0, 'w':0, 'r':0, 'u':0, 'v':0, 'x':0, 's':0, 'g':0, 'i':0}
    d2 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    
    for m in xrange(0, len(n)):
        if n[m] == 'Z':
            d['z'] = d['z'] + 1
        if n[m] == 'W':
            d['w'] = d['w'] + 1
        if n[m] == 'R':
            d['r'] = d['r'] + 1
        if n[m] == 'U':
            d['u'] = d['u'] + 1
        if n[m] == 'V':
            d['v'] = d['v'] + 1
        if n[m] == 'X':
            d['x'] = d['x'] + 1
        if n[m] == 'S':
            d['s'] = d['s'] + 1
        if n[m] == 'G':
            d['g'] = d['g'] + 1
        if n[m] == 'I':
            d['i'] = d['i'] + 1
        if n[m] == 'N':
            d['n'] = d['n'] + 1

    d2[0] = d['z']
    d2[2] = d['w']
    d2[4] = d['u']
    d2[6] = d['x']
    d2[8] = d['g']
    d2[7] = d['s'] - d2[6]
    d2[5] = d['v'] - d2[7]
    d2[3] = d['r'] - d2[4] - d2[0]
    d2[9] = d['i'] - d2[5] - d2[6] - d2[8]
    d2[1] = d['n'] - 2*d2[9] - d2[7]

    p = ''
    for r in xrange(0, 10):
        if d2[r] != 0:
            for q in xrange(0, d2[r]):
                p = p+str(r)
            
    print "Case #{0}: {1}".format(i, p)

exit()
