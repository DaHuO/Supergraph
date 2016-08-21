t=int(raw_input().strip())
for _ in xrange(t):
    print 'Case #{}:'.replace('{}',str(_+1)),
    n=int(raw_input())
    if n==0:
        print 'INSOMNIA'
        continue
    s=set()
    factor=0
    while len(s)<10:
        factor+=1
        for x in str(factor*n):
            if abs(len(s)-len(s|{x}))==1:
                s=s|{x}
    print n*factor
    
