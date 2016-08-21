t=int(input())
cs=1
while t!=0:
    c=0
    s=list(input())
    for i in range(1,len(s)) :
        if(s[i]=='-' and s[i-1]=='+'):
            c+=1
            for j in range(0,i) :
                s[j]='-'
        elif(s[i]=='+' and s[i-1]=='-'):
            c+=1
            for j in range(0,i) :
                s[j]='+'
    if '-' in s:
        print("Case #"+str(cs)+":",c+1)
    else:
        print("Case #"+str(cs)+":",c)
    cs+=1
    t-=1