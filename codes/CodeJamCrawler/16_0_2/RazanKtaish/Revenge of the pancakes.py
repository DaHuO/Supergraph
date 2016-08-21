def flip(s,i):
    r=''
    for j in xrange(i+1):
        if s[j]=='-':
            r=r+'+'
        elif s[j]=='+':
            r=r+'-'
    y=r[::-1]+s[i+1::]
    return y
        

t=int(raw_input())
output=[]

for a0 in xrange(t):
    s=raw_input()
    move=0
    
    while '-' in s:
        
        j=s.index('-')
        if j>0:
            s=flip(s,j-1)
            
        else :
            Reverse_S=s[::-1]
            k=Reverse_S.index('-')
            s=flip(s,len(s)-k-1)
            
        move=move+1
        
    output.append(move)
    

    
for i in xrange(t):
    print 'Case #'+str(i+1)+': '+str(output[i])
