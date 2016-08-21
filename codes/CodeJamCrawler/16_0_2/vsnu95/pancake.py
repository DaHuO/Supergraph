def flip(m,s1):
    s2 = s1[m::-1] + s1[m+1:]
    for n in range(m+1):
        if(s2[n]=='+'):
            s2[n] = '-'
        else:
            s2[n] = '+'
    return s2

t = int(input())
for i in range(t):
    s = list(input())
    l = len(s)
    p = l - 1
    ct = 0
    while(s.count('+') != l):
        q=-1
        while(s[p]=='+'):
            p-=1
        while(s[q+1]=='+'):
            q+=1
        if(q!=-1):
            s = flip(q,s)
            ct += 1
        s= flip(p,s)
        ct+=1
    print("Case #"+str(i+1)+": "+ str(ct))        

def flip(m,s1):
    s2 = s1[m::-1] + s1[m+1:]
    for n in range(m+1):
        if(s2[n]=='+'):
            s2[n] = '-'
        else:
            s2[n] = '+'
    return s2
            
        
    
