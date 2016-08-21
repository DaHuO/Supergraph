t=input()
for i in xrange(t):
    s=raw_input().strip()
    a=[]
    b=[]
    for j in xrange(len(s)):
        a.append(s[j])
    while(len(a)!=0):
        if 'W' in a:
            del a[a.index('T')]
            del a[a.index('W')]
            del a[a.index('O')]
            b.append(2)
            continue
        if 'X' in a:
            del a[a.index('S')]
            del a[a.index('I')]
            del a[a.index('X')]
            b.append(6)
            continue
        if 'Z' in a:
            del a[a.index('Z')]
            del a[a.index('E')]
            del a[a.index('R')]
            del a[a.index('O')]
            b.append(0)
            continue
        if 'U' in a:
            del a[a.index('F')]
            del a[a.index('O')]
            del a[a.index('U')]
            del a[a.index('R')]
            b.append(4)
            continue
        if 'V' in a and 'F' in a:
            del a[a.index('F')]
            del a[a.index('I')]
            del a[a.index('V')]
            del a[a.index('E')]
            b.append(5)
            continue
        if 'O' in a:
            del a[a.index('O')]
            del a[a.index('N')]
            del a[a.index('E')]
            b.append(1)
            continue
        if 'S' in a:
            del a[a.index('S')]
            del a[a.index('E')]
            del a[a.index('V')]
            del a[a.index('E')]
            del a[a.index('N')]
            b.append(7)
            continue
        if 'R' in a:
            del a[a.index('T')]
            del a[a.index('H')]
            del a[a.index('R')]
            del a[a.index('E')]
            del a[a.index('E')]
            b.append(3)
            continue
        if 'N' in a:
            del a[a.index('N')]
            del a[a.index('I')]
            del a[a.index('N')]
            del a[a.index('E')]
            b.append(9)
            continue
        if 'G' in a:
            del a[a.index('E')]
            del a[a.index('I')]
            del a[a.index('G')]
            del a[a.index('H')]
            del a[a.index('T')]
            b.append(8)
            continue
    b.sort()
    char=''
    for j in xrange(len(b)):
        char=char+str(b[j])
    print 'Case #%d: '%(i+1) + char
    del a