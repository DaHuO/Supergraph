def check(ls):
    for i in range(10):
        if ls[i]==0:
            return 0
    return 1
t=input()
for i in range(1,t+1):
    m=input()
    if m==0:
        s="Case #"+str(i)+": INSOMNIA"
        print s
        continue
    ls=[0]*10
    j=1
    for j in range(1,200):
        n=m*j
        s=str(n)
        for k in s:
            ls[int(k)]+=1
        if check(ls):
            s="Case #"+str(i)+": "+str(n)
            print s
            break
