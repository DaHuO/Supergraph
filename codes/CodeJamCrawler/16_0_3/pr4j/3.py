inp = open("C-large.in", "r")
otp = open("out.txt", "w")

t = int(inp.readline())

for _ in range(t):
    n, j = map(int, inp.readline().split())

    otp.write("Case #%d:\n" %(_+1))
    for i in range(2**(n/2-2), 2**(n/2-2)+j):
        s = bin(i)[2:] + '1' + bin(i)[2:] + '1'
        otp.write("%s " %s)
        for j in range(2, 11):
            otp.write("%d " %(j**(n/2)+1))
        otp.write("\n")
        
inp.close()
otp.close()
