f = open('D-small-attempt0.in', 'r')
o = open('out.txt', 'w')
T = f.readline()
T = int(T)
for t in range(1, T+1):
    s = f.readline()
    s = s.split()
    s = map(int, s)

    ans = ""
    
    for i in range(1,s[2]+1):
        ans += str(i)
        if i != s[2]:
            ans += " "
    
    outline = "Case #%d: %s\n" % (t, ans)
    o.write(outline)

o.close()
