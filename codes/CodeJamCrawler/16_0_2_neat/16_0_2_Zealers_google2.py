f1=open("B-large.in")
f2=open("B-large.out","w")
san=[]
for g1 in f1:
    san.append(g1.rstrip('\n'))
a=int(san[0])
for x in range(1,a+1):
    b=san[x]
    count=0
    ans=0
    stack='-'
    for  z in b:
        if(z=='-'):
            count=count+1
            if(stack=='+'):
                ans=ans+1
                stack='-'
        else:
            if(count!=0):
                ans=ans+1
            count=0
            stack='+'
    if(count!=0):
        ans=ans+1
    zz=str(x)
    ans=str(ans)
    f2.write("Case #"+zz+": "+ans+'\n')
f1.close()
f2.close()
