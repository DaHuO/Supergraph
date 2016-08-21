T=int(input())
for t in range(T):
    dic_heights={}
    N=int(input())
    heights=[]
    for j in range(2*N-1):
        temp=list(map(int,input().split()))
        for i in temp:
            if i in dic_heights: dic_heights[i]+=1
            else:
                heights.append(i)
                dic_heights[i]=1
    ans=[]
    for i in heights:
        if (dic_heights[i]%2)==1: ans.append(i)
    ans.sort()
    print("Case #"+str(t+1)+":",end=" ")
    for i in ans:
        print(i,end=" ")
    print()
