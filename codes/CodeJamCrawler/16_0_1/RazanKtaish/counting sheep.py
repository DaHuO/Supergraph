t=int(raw_input())
output=[]
for a1 in xrange(t):
    n=raw_input()
    m=int(n)
    
    s='0123456789'
    r=''
    i=1
    
    test=True
    while s!='':
        g=m*i
        n=str(g)
        
        
        for j in xrange(len(n)):
            if n[j] in s:
                r=r+n[j]
                f=s.index(n[j])
                s=s[:f]+s[f+1:]
        i=i+1
        if g==m*i:
            test=False
            break
        
        
        
        
    if test==True:
        output.append(g)
    else :
        output.append('INSOMNIA')

for i in xrange(t):
    print 'Case #'+str(i+1)+': '+str(output[i])
    
                
                
        
        
