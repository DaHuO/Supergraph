n=input()
res_list=[]
for i in range(n):
    
    a=input()
    res_list.append(a)
counter=0
for a in res_list:
    t=[]
    i=1
    s=a
    while len(t)!=10:
        
        a=s*i
        
        
        i=i+1
        
        while a!=0:
            c=a%10
            a=a//10
            if c not in t:
                
                
                t.append(c)


        if i!=1 and a==s:
            break
       
    if s*(i-1)==0:
        print "Case #"+str(counter+1)+": INSOMNIA"
    else:
        print "Case #"+str(counter+1)+": "+str(s*(i-1))
    counter+=1

