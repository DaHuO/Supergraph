def flip(a):
    sn=''
    for i in a:
        if (i=='+'):
            sn=sn+'-'
        else:
            sn=sn+'+'
    return sn

f=open("B-large.in",'r')
p=f.readlines()
for k in range(int((p[0].split("\n"))[0])):
    i=k+1
    s=(p[i].split("\n"))[0]
    l=s[-1]
    y=len(s)
    w=2
    count=0
    while(w<=len(s)):
        if(s[-w]!=l):
            if(s[0]!=l):
                fp=s[0:-(w-1)][::-1]
                m=flip(fp)
                s=m+s[-(w-1):len(s)]
                count=count+1
            l=s[-w]
        w=w+1
    d=s[0]
    for g in s:
        if g!=d:
            count=count+1
            d=g
    if(s[-1]=='-'):
        count=count+1
    print "Case #"+str(i)+": "+str(count)
f.close()

    
