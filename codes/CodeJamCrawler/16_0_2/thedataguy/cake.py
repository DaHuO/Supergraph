T = int(raw_input())

for j in range(1,T+1):
    string = raw_input()
    p = '+'
    n = '-'
    l = list(string)
    stringTemp = string
    i = 0
    while l.count(p) != len(l):
        i += 1
        s = l[0]
        if s==p:
            lTemp = stringTemp.split(n)
            length = len(lTemp[0])
            for k in range(length):
                l[k] = n
            stringTemp = ''.join(l)
        else:
            lTemp = stringTemp.split(p)
            length = len(lTemp[0])
            for k in range(length):
                l[k] = p
            stringTemp = ''.join(l)
        
    print "Case #{}: {}".format(j,i)
