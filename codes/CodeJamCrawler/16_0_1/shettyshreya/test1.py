k=1
n=int(input())
a=[]
q=[0,1,2,3,4,5,6,7,8,9]
c=[]
c=q[:]
l=1
bo=0
f = open("data2.txt", "w")

for j in range(0,n):
    n1=int(input())
    while len(c)!=0:
        
        x=k*n1
        y=x
        while y>0:
            rem=y%10
            a.append(rem)
            y=y/10
        a1=set(a)
        a2=list(a1)
        for i in a2:
            if i in c:
                c.remove(i)
        a=[]
        k=k+1
        if k>=100:
            bo=1
            break;
    if bo==1:
        print("Case #"+str(j+1)+": "+"INSOMNIA")
        f.write("Case #"+str(j+1)+": "+"INSOMNIA " +"\n")
        
    else:
        print("Case #"+str(j+1)+": "+str(x))
        f.write("Case #"+str(j+1)+": "+str(x)+ "\n")
    k=1
    c=q[:]
    a=[]
    bo=0
f.close()   
        
