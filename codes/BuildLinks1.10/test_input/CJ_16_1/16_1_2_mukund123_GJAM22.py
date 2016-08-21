tc=int(raw_input())
for i in range(tc):
    n=int(raw_input())
    a=[0]*3000
    b=[0]*3000
    for k in range(2*n-1):
        l=map(int,raw_input().split())
        for ll in range(len(l)):
    #        print l[ll],
            a[l[ll]]+=1
    bi=0
    #print ""
    for ll in range(len(a)):
        if a[ll]%2!=0 and a[ll]!=0:
            b[bi]=ll
            bi+=1
    print "Case #" + str(i+1)+":",
    for bb in range(len(b)):
        if(b[bb]!=0):
            print b[bb],
    print ""
