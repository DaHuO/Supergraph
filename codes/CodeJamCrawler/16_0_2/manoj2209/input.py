def change(n,c):
    i=0
    a=list(n)
    while(i<=c):
        if(a[i]=='-'):
            a[i]='+'
        else:
            a[i]='-'
        i+=1
    return ''.join(a)
def te(n):
    i=0
    while(i!=len(n)-1):
        if(n[i]!=n[i+1]):
            return i
        i+=1
    if(n[0]=='+'):
        return -2
    else:
        return -1
t=int(raw_input())
for a in xrange(t):
    n=raw_input()
    count=0
    while(1):
        c=te(n)
        if(c==-1):
            print 'Case #%d: %d'%(a+1,count+1)
            break
        elif c==-2:
            print 'Case #%d: %d'%(a+1,count)
            break
        else:
            n=change(n,c)
        count+=1
