t = input()
for i in range(t):
    c = 0
    x = raw_input()
    a = [0]*len(x)
    for j in range(len(x)):
        if x[j]=='+':
            a[j]=1
    for j in range(len(x)-1,-1,-1):
        f=0
        if a[j]==0:
            k=0
            while a[k]==1:
                a[k]=0
                f=1
                k+=1
                if k==len(a):
                    break
            if f==1:
                c+=1
            n = 0 
            for l in a:
                if l==0:
                    n=1
            if n==0:
                break
            k=0
            while k<=(j/2):
                m = a[k]
                a[k] = a[j-k]
                a[j-k] = m
                k+=1
            c+=1
            for k in range(j+1):
                if a[k]==1:
                    a[k]=0
                else:
                    a[k]=1
            n = 0
            for l in a:
                if l==0:
                    n=1
            if n==0:
                break
    print "Case #"+str(i+1)+": "+str(c)        
