def flip(string, end):
    a=string[end::-1]
    c=[]
    # print(string)
    # print("a=",a)
    # print(end)
    for i in range(0,end+1):
        # print(i)
        if(a[i]=='-'):
            c.append('+')
        else:
            c.append('-')
    for i in range(end+1,len(string)):
        c.append(string[i])
    d=''.join(c)   
    # print("d=",d)
    return d

t=input()
for i in range (0,int(t)):
    n=input()
    k=0;
    for j in range (0,len(n)):
        if(n[-j-1]=="-"):
            if(n[0]=='+'):
                l=0
                while(n[l]=='+'):
                    l+=1
                k+=1;
                n=('-'*l)+n[l:]
            n=flip(n,len(n)-j-1)
            k+=1;
    print("Case #" + str(i+1) + ": " + str(k))
