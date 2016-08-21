
n=32
j=500
r=int('1'*(n-2),2)
q=1
print "Case #1:"
for i in range(int(r**0.5)):
    
    s=bin(i)
    v=s[2:]
    if (len(v)!=(n-2)):
        m1='0'*((n-2)-len(v))
        m2=m1+v
    else:
        m2=v
    s='1'+m2+'1'
    t=[]
    y=[]
    for l in range(2,11):
        w=int(s,l)
        fg=0
        for x in range(2,int((int(w**0.5)+1)**0.5)):
            if(w%x==0):
                fg=1
                y.append(x)
                t.append(w)
                break;
        if(fg==0):
            for x in range(int((int(w**0.5)+1)**0.5),int((int(w**0.5)+1)**0.5)+10):
                if(w%x==0):
                    y.append(x)
                    t.append(w)
                    break;
            
        
    if ((len(y)==9)and (q<=j)):
        print s+" "+' '.join(map(str,y))
        if (q==j):
            break
        q=q+1
    
    
