T=int(input())

for t in range(T):
    k=list(input())
    ans=[]
    ans.append(k[0])
    k=k[1:]
    while len(k)>0:
        temp=k[0]
        k=k[1:]
        if ord(temp)>=ord(ans[0]):
            ans=[temp]+ans
        else: ans.append(temp)
    print("Case #"+str(t+1)+": "+"".join(ans))
