fo = open("A-large.in", "r")
fout=open("output.txt","w")
T=int(fo.readline())
for i in range(T):
    num=int(fo.readline())
    if (num==0):
        fout.write("Case #%d: %s\n"%(i+1,"INSOMNIA"))
    else:
        a=[]
        for j in range(10):
            a.append(0);
        flag=0
        j=1
        numorg=num
        while(flag!=1):
            num=j*numorg
            count=1
            s=str(num)
            leng=len(s)
            for l in range(leng):
                a[int(s[l])]=1
            for l in range(10):
                if(a[l]==1):
                    count=count+1
            if(count==11):
                flag=1
            j=j+1
        fout.write("Case #%d: %d\n"%(i+1,num))
fo.close()
fout.close()
