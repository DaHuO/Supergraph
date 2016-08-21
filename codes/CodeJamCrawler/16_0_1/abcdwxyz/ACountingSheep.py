t=input()

for i in range(t):
    n=input()
    l=[0,1,2,3,4,5,6,7,8,9]
    s=str(n)
    m=1
    if n==0:
        #print "Case #",(i+1),": INSOMNIA"
        print "Case #{}: {}".format(i+1,'INSOMNIA')
        continue
    while(len(l)!=0):
        s=str(n*(m))
        for d in s:
            if int(d) in l:
                l.remove(int(d))
        m+=1
    #print "Case #",(i+1),": ",s
    print "Case #{}: {}".format(i+1,s)
