t=int(raw_input())
p=['0','1','2','3','4','5','6','7','8','9']
for z in range(t):
    a=[]
    s=1
    j=1
    n=raw_input().strip(' ')
    if int(n)==0:
        print 'Case #%i:'%(z+1),'INSOMNIA'
    else:
        x=''
        while s==1:
            x=str(int(n)*j)
            for i in x:
                if a.count(i)==0:
                    a.append(i)
            a.sort()
            if a==p:
                s=0
                break
            j+=1
        print 'Case #%i:'%(z+1),x
