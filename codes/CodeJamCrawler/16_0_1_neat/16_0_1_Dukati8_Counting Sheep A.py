T=int(input())
for i in range (T):
    N=int(input())
    ans="0"
    seen={}
    for j in range (10):
        seen[str(j)]=False
    seencount=0
    if N==0:
        seencount=10
        ans="INSOMNIA"
    while seencount<10:
        ans= str(int(ans)+N)
        for char in ans:
            if not seen[char]:
                seen[char]=True
                seencount+=1
    print ("Case #" + str(i+1) + ": " + ans)
