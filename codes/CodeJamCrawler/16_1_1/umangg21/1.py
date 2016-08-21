t=int(input())
for i in range(t):
    s=input()
    p=[]
    l=len(s)
    p.append(s[0])
    for k in range(1,l):
        if p[0]<=s[k]:
            p.insert(0,s[k])
        else:            
            p.append(s[k])
    print("Case #{}: {}".format(i+1,''.join(p)))
        
