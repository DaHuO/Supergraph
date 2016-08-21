noc=int(input())
for i in range(noc):
    val=int(input())
    if val==0:
        print("Case #%d: INSOMNIA"%(i+1))
        continue
    cnt=[0]*20
    temp=0
    while True:
        temp+=val
        sv=temp
        while sv>0:
            cnt[int(sv%10)]=1
            sv//=10
        flag=True
        for j in range(0,10):
            if cnt[j]==0:
                flag=False
        if flag==True:
            print("Case #%d: %d"%(i+1,temp))
            break
