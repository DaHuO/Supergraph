# cook your code here
t=input()
for j in xrange(t):
    n=input()
    i=1
    f0=f1=f2=f3=f4=f5=f6=f7=f8=f9=0
    count=0
    if n==0:
        print "INSOMNIA"
    else:
        n1=n
        while True:
            strn=str(n1)
            if '0' in strn and f0==0:
                count=count+1
                f0=1
            if '1' in strn and f1==0:
                count=count+1
                f1=1
            if '2' in strn and f2==0:
                count=count+1
                f2=1
            if '3' in strn and f3==0:
                count=count+1
                f3=1
            if '4' in strn and f4==0:
                count=count+1
                f4=1
            if '5' in strn and f5==0:
                count=count+1
                f5=1
            if '6' in strn and f6==0:
                count=count+1
                f6=1
            if '7' in strn and f7==0:
                count=count+1
                f7=1
            if '8' in strn and f8==0:
                count=count+1
                f8=1
            if '9' in strn and f9==0:
                count=count+1
                f9=1
            if count==10:
                break
            i=i+1
            n1=n*i
        
        print n1
    
