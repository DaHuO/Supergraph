import math
t=input()
flag=1

n,m=map(int,raw_input().strip().split(' '))
x=0
print "Case #1:"
for j in xrange(2**(n-1)+1,2**(n),2):
    flag=1
    a=[0,0,0,0,0,0,0,0,0]
    num=int(bin(j)[2:])
    for i in xrange(2,11):
        p=int(str(num),i)
        for k in xrange(2,int(math.sqrt(p))):
            if p%k==0:
                a[i-2]=k
                break
    for i in xrange(9):
        if a[i]==0:
            flag=0

    if flag!=0:
        x+=1
        print num,
        for i in xrange(9):
            print a[i],
        print ""

    del a
    if x==m:
        break