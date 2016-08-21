inFile = open("A-large.in", "r")
outFile = open("aLarge.out", "w")

N = int(inFile.readline())

for i in range(N):
    print i,
    a = int(inFile.readline())
    s = set()
    t = 0
    if a == 0:
        outFile.write("Case #" + str(i+1) + ": " + "INSOMNIA" + "\n")
    else:
        while s != set("0123456789"):
                t += a
                s = s | set(str(t))
        outFile.write("Case #" + str(i+1) + ": " + str(t) + "\n")
    
inFile.close()
outFile.close()
