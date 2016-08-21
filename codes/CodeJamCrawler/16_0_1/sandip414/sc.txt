for i in xrange(int(raw_input())):
    n=int(raw_input())
    if n==0:
        print 'Case #'+str(i+1)+': '+'INSOMNIA'
    else:
        c=1
        num=[0,1,2,3,4,5,6,7,8,9]
        num1=[]
        while(1):
            n1=n*c
            k=n1
            while(n1):
                if(n1%10) not in num1:
                    num1.append(n1%10)
                n1/=10
            num1.sort()
            if num1==num:
                print 'Case #'+str(i+1)+': '+str(k)
                break
            c+=1
        