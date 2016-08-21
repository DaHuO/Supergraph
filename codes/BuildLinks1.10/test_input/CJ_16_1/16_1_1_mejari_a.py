f = open("A-large.in", "r")
t = int(f.readline())
for T in range(t):
    m = 0
    s = f.readline()
    l = len(s)
    ans = ''
    for e in range(l-1):
        if(m <= ord(s[e])):
            ans = s[e] + ans
            m = ord(s[e])
        else:
            ans = ans + s[e]
    
    print("Case #" + str(T+1) + ": " + ans)
