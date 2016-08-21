t=int(raw_input())
output=[]

for a0 in xrange(t):
    n=int(raw_input())
    a=[]
    for i in xrange (2*n-1):
        s=map(int,raw_input().split())
        for j in s:
            a.append(j)
    
    v=set(a)
    v=list(v)
    v.sort()
   
    y=''
    for e in v:
        x=a.count(e)
        if x%2==1:
            y=y+' '+str(e)
    
            
       
    output.append(y)
        
        





for i in xrange(len(output)):
    print 'Case #'+str(i+1)+': '+str(output[i])
