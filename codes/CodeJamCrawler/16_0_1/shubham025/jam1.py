t=input()
case=1
while t:
    t=t-1
    flag=0
    count=set()
    n=input()
    if(n==0):
        #print "Case #%d: %s" % (case,"INSOMNIA")
        #case+=1
        flag=1
    else:
        mul=1
        while len(count)<=9:
            temp=mul*n
            temp1=list(str(temp))
            count.update(temp1)
            mul+=1
    if(flag==0):
        print "Case #%d: %d" % (case,temp)
        case+=1
    else:
        print "Case #%d: %s" % (case,"INSOMNIA")
        case+=1
    
