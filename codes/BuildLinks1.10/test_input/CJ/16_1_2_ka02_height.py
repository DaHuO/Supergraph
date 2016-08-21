t = int(raw_input())
test = t
while t > 0:
    n = int(raw_input())
    a = b = c = []
    
    for i in range (0, (n*2)-1):
        l = map(int, raw_input().split())
        #a.append(l)
        a = a + l
        b = list(set(a))
    
    for i in range(0, len(b)):
        if a.count(b[i]) % 2 != 0:
            c.append(b[i])
            
    c.sort()            
    print "Case #" + str(test - t + 1) + ":",
    for i in range(0, len(c)):
        print c[i],
    print
    t -= 1