n=int(raw_input())
for j in range(0,n):
    num=raw_input()
    x=int(num)
    y=0
    count=1
    endp=0
    arr=[]
    flag=0
    for i in range(0,10):
        arr.append(0)
    while(endp<10):
        for i in num:
            if arr[int(i)]==0:
                arr[int(i)]=1
                endp+=1
        if(endp==10):
            break
        else:
            y=count*x
            num=str(y)
            if(y==0):
                break
            count+=1
    if(endp==10):
        print "case #"+str(j+1)+": "+str(y)
    else:
        print "case #"+str(j+1)+": INSOMNIA"
            
        
