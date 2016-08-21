def countdigits(n,li):
    done=True
    a=1
    number=n
    while done:
        number=n*a
        a=a+1
        str_a=str(number)
        for k in str_a:
            if li[int(k)]!=True:
                li[int(k)]=True
        x=True
        for i in li:
            x=x and i
        done= not x
    return number
T=int(input(''))
for i in range(1,T+1):
    n=int(input(''))
    li=[False for k in range(10)]
    if n==0:
        print "Case #"+str(i)+": INSOMNIA"
    else:
        print "Case #"+str(i)+": "+str(countdigits(n,li))
    
    
