tc=int(raw_input())
for i in range(tc):
    n=int(raw_input())
    m=str(n)
    k=n
    c=1
    if n==0:
        print "Case #"+str(i+1)+":" + " "+"INSOMNIA"
    else:
        while len(set((m)))!=10:
            c=c+1
            n=k*c
            m=m+str(n)
        print "Case #"+str(i+1)+":" + " "+str(n)
        
