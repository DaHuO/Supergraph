inp = open("B-large.in", "r")
otp = open("out.txt", "w")

t = int(inp.readline())

for _ in range(t):
    a = inp.readline().rstrip()

    s = ''
    x = 'x'
    for i in range(len(a)):
        if i > 0 and a[i] == x:
            continue
        else:
            s += a[i]
        x = a[i]

    res = len(s)
    if s[-1] == '+':
        res -= 1
        
    otp.write("Case #%d: %d\n" %(_+1, res))

inp.close()
otp.close()
        
    
