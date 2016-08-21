for tc in range(1,input()+1):
    n=input()
    lis=map(int,raw_input().split())
    t=[]
    for i in range(26):
        t.append([0,chr(ord('A')+i)])
    for i in range(n):
        t[i][0]=lis[i]
    tot=sum(lis)
    rem=0
    pr=0
    print "Case #%d:"%(tc),
    while True:
        t.sort(reverse=True)
        if t[0][0]==0:
            break
        fl=True
        if t[0][0]>=2:
            x=max(t[0][0]-2,t[1][0])
            if 2*x<=tot-rem-2:
                print 2*t[0][1],
                t[0][0]-=2
                rem+=2
                fl=False
                continue
            x=max(t[0][0]-1,t[1][0]-1)
            if fl and 2*x<=tot-rem-2:
                print t[0][1]+t[1][1],
                t[0][0]-=1
                t[1][0]-=1
                rem+=2
                fl=False
                continue
            x=max(t[0][0]-1,t[1][0])
            if fl and 2*x<=tot-rem-1:
                print t[0][1],
                t[0][0]-=1
                rem+=1
                fl=False
                continue
        else:
            if tot-rem==2:
                print t[0][1]+t[1][1],
                t[0][0]-=1
                t[1][0]-=1
                rem+=2
                continue
            else:
                print t[0][1],
                t[0][0]-=1
                rem+=1
                continue
    print

