def maneuver(a,p):
    print("Case #{}:".format(p),end=' ')
    count=0
    while(a.count('+')!=len(a)):
        index=a.index('-')   
        if index!=0:
            temp=list(a[:index])[::-1]

            for i in range(len(temp)):
                if temp[i]=='-':temp[i]='+'
                else:temp[i]='-'
            a=''.join(i for i in temp)+a[index:]
            count+=1
        if '+' in a:    
            index=a.index('+')
            temp=list(a[:index])[::-1]
            for i in range(len(temp)):
                if temp[i]=='-':temp[i]='+'
            a=''.join(i for i in temp)+ a[index:]
            count+=1
        else:
            a='+'*len(a)
            count+=1
    print(count)
    
t=int(input())
p=1
while(p<=t):
    s=input()
    maneuver(s,p)
    p+=1
