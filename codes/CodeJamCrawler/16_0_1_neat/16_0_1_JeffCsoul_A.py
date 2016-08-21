fIn = open("A-large.in","r")
fOut = open("answerA.out","w")
N = eval(fIn.readline().strip())
for T in range(N):
    m = eval(fIn.readline().strip())
    num = set()
    ans = -1
    for i in range(1,20000):
        temp = str(m * i)
        for x in temp:
            num = num | {x}
        if len(num) == 10:
            ans = m * i
            break
    fOut.write("Case #" + str(T + 1) + ": ")
    if ans == -1:
        fOut.write("INSOMNIA\n")
    else:
        fOut.write(str(ans) +'\n')



