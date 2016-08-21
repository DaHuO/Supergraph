def mult(m):
    d=2
    while 1:
        if m%d==0:
            return d
        elif d>7000:
            return m
        else:
            d=d+1
print "Case #1:"    
count=0
ntd=[]
test=input()
while test!=0:
    test=test-1
    l22,j = map(int,raw_input().split(' '))
    while j!=0:
        s=[1]
        n = l22-2
        for i in xrange(1<<n):
            s=s+ list(bin(i)[2:].zfill(n))
            s.append(1)
            t=[]
            for ip in range(0,len(s)):
                t.append(int(s[ip]))
            for i3 in range(2,11):
                number=0
                for ji in range(0,len(t)):
                    number=number+(t[len(t)-ji-1]*(i3**ji))
                if mult(number)!=number:
                    count=count+1
                    ntd.append(mult(number))
                else:
                    count=0
                    ntd=[]
                    break
            if count<9:
                j=j
                s=[1]
            else:
                j=j-1
                nn=""
                for ip in range(0,len(t)):
                    nn=nn+str(t[ip])
                print nn,
                for ikk in ntd:
                    print ikk,
                print 
                count=0
                ntd=[]
                s=[1]
                if j==0:
                    break