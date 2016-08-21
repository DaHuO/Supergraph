t=int(raw_input())
d=set(map(str,range(10)))
for i in range(t):
    n = int(raw_input())
    if n==0:
        print "Case #%s: INSOMNIA" % (i+1)
        continue
    s=set()
    k=0
    while s!=d:
        k+=1
        s|=set(list(str(k*n)))
    print "Case #%s: %s" % (i+1,k*n)
