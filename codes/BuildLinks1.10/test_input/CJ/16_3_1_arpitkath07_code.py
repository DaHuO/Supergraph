def g(s):
    n=sum(s)
    for i in range(len(s)):
        if s[i]>n/2:
            return True
    return False
def f(n):
    s=map(int,input().split())
    s=list(s)
    t=[]
    while sum(s)!=0:
        mx = max(s)
        mx_in = s.index(mx)
        s[mx_in] = 0
        smx = max(s)
        smx_in = s.index(smx)
        if mx == smx:
            t.append(str(mx_in)+str(smx_in))
            s[mx_in]=mx-1
            s[smx_in]=smx-1
            if g(s):
                del t[-1]
                s[smx_in]+=1
                t.append(str(mx_in))
        else:
            t.append(str(mx_in))
            s[mx_in]=mx-1
    return " ".join(str(i) for i in t)
def ans(n):
    res=f(n)
    dict={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    t=[]
    for i in res.split():
        s=list(i)
        s=map(int,s)
        m=''
        for j in s:
            m+=str(dict[j])
        t.append(m)
    return " ".join(str(i) for i in t)
t=int(input())
for i in range(1,t+1):
    n=int(input())
    print("Case #%d: %s"%(i,ans(n)))
    
                     