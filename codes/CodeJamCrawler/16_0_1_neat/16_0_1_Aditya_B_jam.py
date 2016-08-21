d1=[]
def check(t):
    ti=[]
    x=t
    while(x):
        z=x%10
        x=x/10
        if((z not in li) and (z not in ti) ):
            ti.append(z)
      
    li.extend(ti)
    if(len(li)==10):
        return 1
    
        
    
    
 


def  main(x):    
    for i in range(1,100):
        z=x*i
        m=check(z)
        if(m==1):
            print z
            return 
    if(i>=99):
        print 'INSOMNIA'
        return
        
fo = open("A-large.in", "r")

d2=fo.readlines()
for i in range(0,len(d2)):
    d2[i]=int(d2[i].rstrip())

t=d2[0]

for j in range(1,t+1):
    li=[]
    x=d2[j]
    print 'Case #'+str(j)+': ',
    main(x)

    
