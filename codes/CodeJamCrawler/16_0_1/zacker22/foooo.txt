n=int(input())
from collections import defaultdict
M=[]
for i in range(n):
    M.append(int(input()))
j=0    
for m in M:
    
    lis=[]
    D=defaultdict(int)
    j=0
    while (len(lis)!=10):
        curr=m*(j+1)
        if D[curr]==1:
            st="INSOMNIA"
            break
        lis+=(list(str(curr)))
        lis=list(set(lis))
        D[curr]=1
        st=str(curr)
        j+=1
    print("Case #{}: {}".format(j+1,st))
    j+=1