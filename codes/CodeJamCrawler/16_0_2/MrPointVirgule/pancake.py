t=int(input())
for k in range(1,t+1):
    s=list(input())
    r=0
    while set(s)!=set('+'):
        i = 0
        if s[0]=='+':
            while i<len(s) and s[i]=='+':
                s[i]='-'
                i+=1
        else:
            while i<len(s) and s[i] == '-':
                s[i] = '+'
                i += 1
        r+=1
    print("Case #"+str(k)+": "+str(r))