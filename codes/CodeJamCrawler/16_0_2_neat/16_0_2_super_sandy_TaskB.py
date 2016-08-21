def Convert(a):
    n= len(a)
    s = '1' * n
    x = int(a,2) ^ int(s,2)
    return '{:0{}b}'.format(x, n)

t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    n = len(s)
    bs =''
       
    for j in s:
        bs+= ('1' if j=='+' else '0')
        
    l=0
    for j in range(n-1, -1, -1):
        if bs[j]=='0':
            y = Convert(bs[:j+1])
            bs = y + bs[-j+1:]
            l+=1
    print "Case #{}: {}".format(i, l)

