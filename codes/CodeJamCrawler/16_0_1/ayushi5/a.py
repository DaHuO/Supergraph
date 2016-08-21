t=int(input())
for j in range (t):
    n=input()
    s=set()
    l=list()
    if n=='0':
        print("Case #{}: {}".format(j+1,"INSOMNIA"))
    else:
        a=int(n)
        i=1
        while(True):
            b=a*i
            for char in str(b):
                s.add(char)
            #print(s)
            if len(s)==10:
                print("Case #{}: {}".format(j+1,b))
                break
            i+=1
        
            
        
            