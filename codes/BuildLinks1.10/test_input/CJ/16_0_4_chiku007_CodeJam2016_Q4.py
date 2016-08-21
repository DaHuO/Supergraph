for tc in range(int(raw_input())):
    k,c,s=map(int,raw_input().split())
    ans="Case #"+str(tc+1)+": "
    if k==s:
        for i in range(1,s+1):
            ans+=str(i)+" "
    else:
        ans+="IMPOSSIBLE"
    print ans
