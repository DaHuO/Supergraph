f = open('B-large.in', 'r')
o = open('out.txt', 'w')
T = f.readline()
T = int(T)
for t in range(1, T+1):
    s = f.readline()
#    s = s.split()
#    s = map(int, s)
    s = s[:-1]


    ans = 0
    
    curr = s[0]
    for i in xrange(len(s)): 
        if s[i] != curr:
            if t == 2: 
                print s[i], ',', curr, ',', ans
            ans += 1
            curr = s[i]             
            
    if curr == "-":
        ans += 1
    if t == 2: 
        print ans
                     
    outline = "Case #%d: %d\n" % (t, ans)
    o.write(outline)

o.close()
