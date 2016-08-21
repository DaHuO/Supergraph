for tcs in range(int(raw_input())):
    a,b,c=map(int,raw_input().split())
    ans="Case #"+str(tcs+1)+": "
    if a==c:
        for i in range(1,c+1):
            ans+=str(i)+" "
    else:
        ans+="IMPOSSIBLE"
    print ans
