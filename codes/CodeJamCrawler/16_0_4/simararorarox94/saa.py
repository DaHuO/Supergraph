t=input()
xx=1
while t>0:
    k,c,s=map(int,raw_input().split())
    ans=1
    temp=pow(k,c-1)
    print "Case #%d: %d" %(xx,ans),
    for i in range(1,s):
        print ans+temp,
        ans+=temp
    print
    xx+=1
    t-=1
