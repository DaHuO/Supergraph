t = input()
for T in xrange(1,t+1):
    print "Case #"+str(T)+":",
    s = list(raw_input())+['#']
    temp = 0
    ans = 0
    while(s[0]=='+'):
        s.pop(0)
        temp+=1
    while(s[0]!='#'):
        x = 0
        while(s[0]=='-'):
            s.pop(0)
            x+=1
        if(temp!=0):
            ans+=2
        else:
            ans+=1
        temp+=x
        while(s[0]=='+'):
            s.pop(0)
            temp+=1
    print ans
        
