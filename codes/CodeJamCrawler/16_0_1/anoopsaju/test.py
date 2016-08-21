for j in range(int(raw_input())):
    check=[0 for _ in range(10)]
    x=int(raw_input())
    i=1
    if(x==0):
        temp="INSOMNIA"
        print "Case #%d: %s" %((j+1),temp)
        continue
    count=0
    while((sum(check)<=9)):
        count+=1
        num=x*i
        temp=num
        while(int(num/10)!=0):
            check[num%10]=1
            num=num/10
        check[num%10]=1
        i+=1
    print "Case #%d: %s" %((j+1),temp)
