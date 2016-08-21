def ciel(x):
    if (x!=int(x)):
        return int(x+1)
    return x

t = int(raw_input())
u = 0
while u<t:
    u+=1
    print "Case #%d:" %u,
    s = raw_input()
    zs = 0
    gs = 0
    xs = 0
    ss = 0
    ws = 0
    hs = 0
    vs = 0
    fs = 0
    ns = 0
    os = 0
    #0-z, 8-g, 6-x, 7-s, 2-w, 3-h, 5-v, 4-f, 1-o, 9-n
    for i in s:
        if i=='Z':
            zs+=1
        if i=='G':
            gs+=1
        if i=='X':
            xs+=1
        if i=='S':
            ss+=1
        if i=='W':
            ws+=1
        if i=='H':
            hs+=1
        if i=='V':
            vs+=1
        if i=='F':
            fs+=1
        if i=='N':
            ns+=1
        if i=='O':
            os+=1
    n0 = zs
    n8 = gs
    n6 = xs
    n7 = ss-n6
    n2 = ws
    n3 = hs-n8
    n5 = vs-n7
    n4 = fs-n5
    n1 = os-n0-n2-n4
    n9 = (ns-n7-n1)/2
    print '0'*n0+'1'*n1+'2'*n2+'3'*n3+'4'*n4+'5'*n5+'6'*n6+'7'*n7+'8'*n8+'9'*n9
