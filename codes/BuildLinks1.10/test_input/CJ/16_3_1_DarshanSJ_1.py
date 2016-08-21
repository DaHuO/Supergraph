t=input()
case=1
def sindex(n,l,i):
    max=-1
    maxI=-1
    for x in xrange(n):
        if x!=i and l[x]>max:
            max=l[x]
            maxI=x
    return maxI
def possible(n,l,i):
    if l[i]<2:
        return False
    l[i]-=2
    if max(l)>sum(l)/2.0:
        l[i]+=2
        return False
    l[i]+=2
    return True

def ipossible(n,l,i,x):
    if l[i]<1 or l[x]<1:
        return False
    l[i]-=1
    l[x]-=1
    if max(l)>sum(l)/2.0:
        l[i]+=1
        l[x]+=1
        return False
    l[i]+=1
    l[x]+=1
    return True
    
        
def process(n,l):
    count=sum(l)
    out=''
    while count>0:
        i=l.index(max(l))
        if possible(n,l,i):
            #print 'if1'
            l[i]-=2
            out+=' '+chr(ord('A')+i)*2
            count-=2
            continue
        x=sindex(n,l,i)
        if ipossible(n,l,i,x):
            #print 'if2'
            l[i]-=1
            l[x]-=1
            out+=' '+chr(ord('A')+i)+chr(ord('A')+x)
            count-=2
        else:
            #print 'else'
            l[i]-=1
            out+=' '+chr(ord('A')+i)
            count-=1
    #out=out.rstrip()
    return out
        
    
while case<=t:
    n=input()
    l=map(int,raw_input().strip().split())
    out=process(n,l)
    print 'Case #'+str(case)+':'+out
    case+=1
