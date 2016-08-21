# cook your code here
t = int(raw_input())
for i in xrange(t):
    a = raw_input()
    b = list(a)
    c = []
    if b[0]>b[1]:
        c.append(b[0])
        c.append(b[1])
    else:
        c.append(b[1])
        c.append(b[0])
    for j in range(2,len(b)):
        if b[j] >= c[0]:
            c.insert(0, b[j])
        else:
            c.insert(j, b[j])
    print 'Case #'+ str(i+1)+':',  ''.join(c)