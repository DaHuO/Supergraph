#khf
#jenlef
ld = 0
lgs = []
n=int(raw_input())
for n in range(0,n):
    a=int(raw_input())
    
    if(a==0):
        print 'Case #%s: INSOMNIA'%(n+1)
    else:
        num=[0,1,2,3,4,5,6,7,8,9]
        for k in range(1,100):
            b=a*k
            
            while(b!=0):
                rem=b%10
                b=b/10
                if (rem in num):
                    num.remove(rem)
                    if (len(num)==0):
                        break
            if (len(num)==0):
                break

            
            
        print'Case #%s: %s'%(n+1,k*a)
