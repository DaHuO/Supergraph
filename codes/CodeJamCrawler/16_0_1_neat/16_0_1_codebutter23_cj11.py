t= input()
def sleep(t):
    
    for i in range(1,t+1):
        l=[0,1,2,3,4,5,6,7,8,9]
        n=input()
        if n==0:
            print "Case #" + str(i) + ": "+"INSOMNIA"
            continue
        
        ctr=1
        while len(l)>0:
            k=ctr*n
            while k!=0:
                if k%10 in l:
                    l.remove(k%10)
                k=k/10
            ctr+=1
        print "Case #" +str(i) +": " + str((ctr-1)*n)

sleep(t)
