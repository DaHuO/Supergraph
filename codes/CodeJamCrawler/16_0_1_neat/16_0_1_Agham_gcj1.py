ans=[]
for i in range(1,1000002):
    h=[0 for j in range(10)]
    n=i
    temp=n
    j=1
    while h.count(0):
        while n:
            h[n%10]=1
            n=n//10
        j=j+1
        n=temp*j
    ans.append(n-temp)
#print (ans)
t=int(input())
for i in range(t):
    n=int(input())
    if not n:
        print('Case #'+str(i+1)+': INSOMNIA')
    else:
        print('Case #'+str(i+1)+': '+str(ans[n-1]))