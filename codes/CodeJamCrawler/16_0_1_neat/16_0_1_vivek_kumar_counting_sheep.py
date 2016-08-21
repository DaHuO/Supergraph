test=input()
t=0
while(t<test):
    num = input()
    list1=map(int,str(num))
    a=[0,1,2,3,4,5,6,7,8,9]
    flag=0
    i=2
    value=0
    while(num!=0 and i<=1000000):
        if set(a)==set(list1):
            flag=1
            value=num*(i-1)
            break
        else:
            list2=map(int,str(num*i))
            list1=list1+list2
        i=i+1
    if(flag==1):
        print "Case #%d: %d" %((t+1),value)
    else:
        print "Case #%d: INSOMNIA" %(t+1) 
    t=t+1
