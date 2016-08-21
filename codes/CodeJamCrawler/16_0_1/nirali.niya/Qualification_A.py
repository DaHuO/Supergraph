T=int(input())
count=0
for _ in range(T):
    N=int(input())
    dic={}
    for j in list(str(N)):
        if j in dic: dic[j]+=1
        else: dic[j]=1
    n_old=N
    i=0
    count+=1
    while len(dic)!=10:
        #print(n_old,dic)
        n_new=n_old+N
        if n_new==n_old:
            i=1
            break
        for j in list(str(n_new)):
            if j in dic: dic[j]+=1
            else: dic[j]=1
        n_old=n_new
    print("Case #"+str(count)+": ",end="")
    if i==1: print("INSOMNIA")
    else: print(n_old)
