T=int(input())
for i in range(T):
    K,C,S=input().split(' ')
    K,C,S=int(K),int(C),int(S)
    res=''
    idx=1
    for j in range(K):
        res=res+' '+str(idx)
        idx=idx+K**(C-1)
    print('Case #'+str(i+1)+':'+res)
    
