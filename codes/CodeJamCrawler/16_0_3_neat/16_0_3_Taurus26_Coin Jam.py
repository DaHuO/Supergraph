File=open("C-large.txt",'w')
T=int(raw_input())
for t in range(T):
    N,J=[int(i) for i in (raw_input().split())]
    print >> File, "Case #%d:" %(t+1)
    
    l=str(10**((N-2)/2))
    r=l[::-1]
    j=0
    while j<J:
        jamcoin=l+r
        print >> File, "%s %d %d %d %d %d %d %d %d %d" %(jamcoin,3,4,5,6,7,8,9,10,11)
        j=j+1
        dec=int(l,2)
        dec=dec+1
        l=bin(dec)[2:]
        r=l[::-1]
        if len(l)*2>N:
            break
File.close()
