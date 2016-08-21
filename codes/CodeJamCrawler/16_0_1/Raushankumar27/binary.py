t=int(input())
case=1
while(t>0):
    
    t-=1
    n=int(input())
    if(n==0):
        print("Case #"+str(case)+": INSOMNIA")
        case+=1 
    else:
        a=set()
        z=n
        i=1
        while(True):
            p=list(str(z))
            #print(z)
            a.update(p)
            #print(a)
            if(len(a)==10):
                break
            i=i+1
            z=n*i
        print("Case #"+str(case)+": "+str(z))
        case+=1 