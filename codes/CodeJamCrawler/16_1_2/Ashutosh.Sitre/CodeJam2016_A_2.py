for tc in range(int(raw_input())):
    n=int(raw_input())
    a=[]
    for i in range(2*n -1):
        b=map(int,raw_input().split())
        a.append(b)
    b=[]
    for i in a:
        for x in i:
            b.append(x)
    c=set(b)
    ans=[]
    for i in c:
        if b.count(i)%2!=0:
            ans.append(i)
    print "Case #"+str(tc+1)+": "+" ".join(str(i) for i in sorted(ans))
