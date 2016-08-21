t=int(input())
for t in range(t):
    a=input()
    c=0
    l=1
    d=set(['-'])
    e=[]
    for i in range(len(a)):
        e.append(a[i])
    else:
        while(5>0):
            if len(set(e))==1:
                break
            if len(e)==1:
                break
            if e[l-1]!=e[l]:
                c+=1
                e=e[l:]
                l=0
            l+=1
        if set(e)==d:
            c+=1
    print('Case #',end='')
    print(t+1,end='')
    print(': ',end='')
    
    print(c)
