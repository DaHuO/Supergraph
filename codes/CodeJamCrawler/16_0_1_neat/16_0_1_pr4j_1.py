inp = open("A-large.in", "r")
otp = open("out.txt", "w")

t = int(inp.readline())

for _ in range(t):
    n = int(inp.readline())

    if n == 0:
        otp.write("Case #%d: INSOMNIA\n" %(_+1))
        continue
    
    s = set()
    a = n
    while ( True ):
        b = list(str(a))
        for i in range(len(b)):
            s.add(b[i])
        if ( len(s) == 10 ):
            break
        a += n

    otp.write("Case #%d: %d\n" %(_+1, a))

inp.close()
otp.close()
        
    
