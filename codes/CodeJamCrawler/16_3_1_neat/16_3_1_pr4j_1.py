import string

alp = string.ascii_uppercase 
inp = open("A-large.in", "r")
otp = open("out.txt", "w")

t = int(inp.readline())

for _ in range(t):
    n = int(inp.readline())
    x = map(int, inp.readline().split())
    a = []
    for i in range(n):
        a.append( [x[i],alp[i]] )

    
    a.sort(reverse=True)
    otp.write("Case #%d: "%(_+1))
    for i in range(n-1):
        if a[0][0] != 1:
            for j in range(a[i][0]-a[i+1][0]):
                for k in range(i+1):
                    a[k][0]-=1
                    otp.write("%c "%(a[k][1]))
    
    for i in range(a[0][0]):
        for j in range(n-2):
            a[j][0] -= 1
            otp.write("%c "%(a[j][1]))
        otp.write("%c%c "%(a[n-2][1],a[n-1][1]))
        a[n-2][0]-=1
        a[n-1][0]-=1
    print a
    otp.write("\n")


inp.close()
otp.close()
        
    
