t = int(input())
for i in range(1,t+1):
    n = int(input())
    m = n
    d = set()
    while len(d) < 10:
        for c in str(m):
            d.add(c)
        m+=n
        if m == n:
            break
    s = str(m-n)
    if len(d) < 10:
        s = 'INSOMNIA'
    print('Case #%d: %s' %(i,s))
