dans=""
for tc in range(int(raw_input())):
    n=int(raw_input())
    ans=""
    if n==0:
        ans="INSOMNIA"
    else:
        s=set()
        d=str(n)
        j=2
        while(len(s)<10):
            q=set(d)
            for i in q:
                s.add(i)
            d=str(j*int(n))
            j+=1
        ans=str(int(d)-n)
    dans+= "Case #"+str(tc+1)+": "+ans+"\n"
print dans
