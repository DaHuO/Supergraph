t=int(raw_input())
for j in range(1,t+1):
    n = int(raw_input())
    name=""
    if(n==0):
        p="Case "+"#"+str(j)+": INSOMNIA"
    else:
        ls=["0","1","2","3","4","5","6","7","8","9"]
        a=1
        while(True):
            if len(ls) != 0:
                name=str(a*n)
                for i in range(0,len(name)):
                    if name[i] in ls:
                        ls.remove(name[i])
            else:
                break;
            a=a+1
            p="Case "+"#"+str(j)+": "+name
    print (p)
    t=t-1