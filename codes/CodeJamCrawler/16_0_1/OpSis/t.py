def splt(a):
    l = []
    while(a != 0):
        l.append(a % 10)
        a = a / 10
    return l
        
def func(n):
    lis = []
    i = 1
    if n == 0:
        return 'INSOMNIA'
    
    while True:
        m = splt(n * i)
        for j in range(len(m)):
            if m[j] not in lis:
                lis.append(m[j])
        i = i + 1
        if len(lis) == 10:
            break
    return n * (i-1) 
        
t = long(raw_input())
s = []
for i in range(t):
    s.append(long(raw_input()))
    
for k in range(t):
    m = splt(s[k])
    print 'Case#'+str(k+1)+':'+str(func(s[k]))
