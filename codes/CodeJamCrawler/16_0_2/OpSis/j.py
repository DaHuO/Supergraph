def func(n):
    lis = []
    out = []
    i = 1
    count = 0
    lis = list(n)
    lis.reverse()
    while lis.count('-') != 0:
        count = count + 1
        out.append(lis.pop())
        i = 1
        while True:
            if not lis:
                break
            elif out[len(out)-1] == lis[len(lis)-1]:
                out.append(lis.pop())
            else:
                break
            i = i + 1

        if lis:
            c = lis[len(lis)-1]
            for j in range(len(out)):
                out[j] = c
        else:
            for j in range(len(out)):
                if out[j] == '+':
                    out[j] = '-'
                else:
                    out[j] = '+'
    
        ln = len(out)
        for k in range(ln):
            lis.append(out.pop())
            
    return count
        
t = long(raw_input())
s = []
out = []
for i in range(t):
    s.append(raw_input())
    out.append(func(s[i]))
    

for k in range(t):
    print 'Case #'+str(k+1)+': '+str(out[k])
