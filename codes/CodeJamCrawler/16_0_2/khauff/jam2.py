fo = open("B-large.in", "r")
fout=open("output2.txt","w")
T=int(fo.readline())
for i in range(T):
    a=list(fo.readline().strip())
    flag=0
    flips=0
    leng=len(a)
    count=0
    for l in range(leng):
        if(a[l]=='+'):
            count=count+1
    if(count==0 or count==leng):
        flag=1
    while(flag!=1):
        if(a[0]=='+'):
            j=0
            while(a[j]!='-'):
                a[j]='-'
                j=j+1
        else:
            j=0
            while(a[j]!='+'):
                a[j]='+'
                j=j+1
        leng=len(a)
        count=0
        flips=flips+1
        for l in range(leng):
            if(a[l]=='+'):
                count=count+1
        if(count==0 or count==leng):
            flag=1
    if(count==0):
        fout.write("Case #%d: %d\n"%(i+1,flips+1))
    else:
        fout.write("Case #%d: %d\n"%(i+1,flips))
fo.close()
fout.close()
