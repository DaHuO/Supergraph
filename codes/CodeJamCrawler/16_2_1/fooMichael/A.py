t = int(input())  
for i in range(1, t + 1):
    s = list(input())
    
    digs = list(("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"))

    resdigs = []
    zc = s.count('Z')
    for j in range(zc):
        for ch in digs[0]:
            s[s.index(ch)] = '#'
        resdigs.append(0)
    xc = s.count('X')
    for j in range(xc):
        for ch in digs[6]:
            s[s.index(ch)] = '#'
        resdigs.append(6)
    wc = s.count('W')
    for j in range(wc):
        for ch in digs[2]:
            s[s.index(ch)] = '#'
        resdigs.append(2)
    uc = s.count('U')
    for j in range(uc):
        for ch in digs[4]:
            s[s.index(ch)] = '#'
        resdigs.append(4)
    rc = s.count('R')
    for j in range(rc):
        for ch in digs[3]:
            s[s.index(ch)] = '#'
        resdigs.append(3)
    fc = s.count('F')
    for j in range(fc):
        for ch in digs[5]:
            s[s.index(ch)] = '#'
        resdigs.append(5)
    sc = s.count('S')
    for j in range(sc):
        for ch in digs[7]:
            s[s.index(ch)] = '#'
        resdigs.append(7)
    oc = s.count('O')
    for j in range(oc):
        for ch in digs[1]:
            s[s.index(ch)] = '#'
        resdigs.append(1)
    gc = s.count('G')
    for j in range(gc):
        for ch in digs[8]:
            s[s.index(ch)] = '#'
        resdigs.append(8)
    ic = s.count('I')
    for j in range(ic):
        for ch in digs[9]:
            s[s.index(ch)] = '#'
        resdigs.append(9)
    

    resdigs.sort()
    res = ''.join([str(ni) for ni in resdigs])
    print('Case #{}: {}'.format(i, res))

    
