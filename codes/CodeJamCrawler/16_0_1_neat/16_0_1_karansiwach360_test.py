t=int(raw_input())
for i in range(0,t):
    n=int(raw_input())
    print "Case #"+str(i+1)+":",
    count=0
    if n is 0:
        print "INSOMNIA"
    else:
        arr=[0,0,0,0,0,0,0,0,0,0]
        j=0
        while count<10:
            srr=str((j+1)*n)
            l=len(srr)
            for k in range(0,l):
                if arr[int(srr[k])] is 0:
                    arr[int(srr[k])]=1
                    count=count+1    
            j=j+1
        print j*n
