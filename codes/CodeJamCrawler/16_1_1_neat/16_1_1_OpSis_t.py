def func(n):
    lis = []
    temp = list(n)
    temp.reverse()
    lis.append(temp.pop())
    for i in range(len(n)-1):
        c = temp.pop()
        if c >= lis[0]:
            lis.insert(0, c)
        else:
            lis.append(c)
    return lis

t = long(raw_input())
s = []

for i in range(t):
    s.append(raw_input())

for k in range(t):
    print 'Case #'+str(k+1)+': '+''.join(func(s[k]))
