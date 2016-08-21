L=[]
for j in range(int(input())):
    n=int(input())    
    m=[]
    for x in range(n*2-1):
        v=[int(x) for x in input().split()]
        m+=(v)
    L.append(m)
for j in range(len(L)):
    s=L[j]
    q=[]
    for i in set(s):
        if s.count(i)%2==1:
            q.append(i)
    q=sorted(q)
    b=""        
    for i in q:
        b+=str(i)+" "
        
    print("Case #{}: {}".format(j+1,b))