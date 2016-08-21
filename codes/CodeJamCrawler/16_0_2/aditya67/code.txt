t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    if n==0:
        print 'Case #'+ str(i+1)+': INSOMNIA'
        continue
    a = str(n)
    x=2
    b = list(set(a))
    while(len(b)!=10):
        k = n*x
        x+=1
        a = str(k)
        c = list(set(a))
        for j in c:
            b.append(j)
        b = list(set(b))
    print 'Case #'+ str(i+1)+': '+str(k)