
def arrange(s):
    ls=s.split()
    d=dict()
    for i in ls:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    f=[]
    for i in d:
        if d[i]%2!=0:
            f.append(int(i))
        else: continue
    c=sorted(f)
    m=[]
    for i in c:
        m.append(str(i))
    return ' '.join(m)
        










t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    s=''
    for j in range(2*n-1):
        a=raw_input()
        s=s+a+' '
    print "Case #{}: {}".format(i+1, arrange(s))
