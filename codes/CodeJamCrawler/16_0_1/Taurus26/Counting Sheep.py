File=open("A-large.txt",'w')
T=int(raw_input())
for t in range(T):
    N=int(raw_input())
    seen=[]
    k=1
    if N==0:
        print >> File, "Case #%d: INSOMNIA" %(t+1)
    else:
        while not len(seen)==10:
            n=k*N
            for i in str(n):
                if not int(i) in seen:
                    seen.append(int(i))
            k=k+1
        print >> File, "Case #%d: %d" %(t+1,n)
File.close()
