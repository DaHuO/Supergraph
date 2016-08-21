t=int(raw_input())
output=[]

for a0 in xrange(t):
    s=raw_input()
    a=s[0]
    for i in xrange(1,len(s)):
        if s[i]<a[0]:
            a=a+s[i]
        else :
            a=s[i]+a
            
       
    output.append(a)
        
        





for i in xrange(len(output)):
    print 'Case #'+str(i+1)+': '+str(output[i])

