f=open('Ip.txt','w')
for _ in xrange(input()):
    n=input()
    li=[]
    xx=list(map(int,raw_input().split()))
    ct=[]
    for i in xrange(n):
        li.append(chr(65+i)*xx[i])
        ct.append(xx[i])
    s=sum(ct)
    print "Case #%d:"%(_+1),
    while ct!=[0]*n:
        ch=''
        a=max(ct)
        if a==1 and ct.count(a)==n:
            if sum(ct)%2==0:
                for i in xrange(0,n,2):
                    ch+=li[i][0]
                    ch+=li[i+1][0]
                print ch,
            else:
                print li[0][0],
                for i in xrange(1,n,2):
                    ch+=li[i][0]
                    ch+=li[i+1][0]
                print ch,
            break
        elif ct.count(a)>1:
            flag=0
            for i in xrange(n):
                if flag==2:
                    break
                if ct[i]==a:
                    ct[i]-=1
                    ch+=li[i][0]
                    li[i]=li[i][0]*(ct[i])
                    flag+=1
        elif ct.count(a-1)>0:
            for i in xrange(n):
                if ct[i]==a:
                    ct[i]-=1
                    ch=li[i][0]
                    li[i]=li[i][0]*(ct[i])
                    break
        else:
            for i in xrange(n):
                if ct[i]==a:
                    ct[i]-=2
                    ch=li[i][0]*2
                    li[i]=li[i][0]*(ct[i])
                    break
        print ch,
    print 
f.close()
