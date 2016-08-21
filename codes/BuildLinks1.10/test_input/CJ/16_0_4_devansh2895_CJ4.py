t=int(input())
cs=1
while(t!=0):
    k,c,s=input().split(" ")
    k=int(k)
    c=int(c)
    s=int(s)
    print("Case #"+str(cs)+": ",end='')
    for i in range(1,k+1) :
        print(i,end=' ')
    print()
    cs+=1
    t-=1