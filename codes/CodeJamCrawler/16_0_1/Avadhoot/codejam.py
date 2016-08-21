T=int(raw_input())
for i in range(T):
    N=int(raw_input())
    digits=set()
    c=1
    n=N
    if N==0:
        print "case #"+str(i+1)+": INSOMNIA"
        continue
    while len(digits)!=10:
        for j in str(n):
            digits.add(j)
            #print digits
        n=c*N
        c+=1
    #print n,c,N
    c-=2
    n=c*N
    print "case #"+str(i+1)+": "+str(n)
