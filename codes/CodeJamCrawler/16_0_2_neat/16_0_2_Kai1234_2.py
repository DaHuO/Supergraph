def count_inversion(s):
    t=1
    if(s[0]=='+'):
        t=0
    n=0
    for i in range(1,len(s)):
        if(t==1 and s[i]=='+'):
            t=0
            n+=1
        elif(t==0 and s[i]=='-'):
            t=1
            n+=1
    return n


num=int(input())
for i in range(1,num+1):
    s=input()+"+"
    n=count_inversion(s)
    print("Case #"+str(i)+": "+str(n))
