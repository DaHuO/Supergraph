lis=int(raw_input())
for j in range(0,lis):
    C = raw_input().strip()
    C=C[::-1]
    N=len(C)
    x=C[0]
    count=0
    i=0
    while i<N:
        if(count==0):
            if('-'==C[i]):
                count+=1
        while(x==C[i]):
            i=i+1
            if(i==N):
                break
        if(i==N):
            break
        if(x!=C[i]):
            count=count+1;
            x=C[i]
    print "Case #"+str(j+1)+": "+str(count)
