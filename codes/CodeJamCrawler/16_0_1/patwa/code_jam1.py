for t in range(int(raw_input())):
    n=int(raw_input())
    if n==0:
        print "Case #%d: INSOMNIA"%(t+1)
    else:
        list1=[0,1,2,3,4,5,6,7,8,9]
        list2=[]
        for i in range(1,1000000):
            a=i*n
            b=a
            a=list(str(a))
            for j in range(len(a)):
                list2.append(int(a[j]))
            #print list2
            list2=list(set(sorted(list2)))
            if list1==list2:
                print "Case #%d: %d"%((t+1),b)
                break

        
        
