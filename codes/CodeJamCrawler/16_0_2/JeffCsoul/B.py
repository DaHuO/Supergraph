fIn = open("B-large.in","r")
fOut = open("answerB.txt","w")
n = eval(fIn.readline().strip())
for T in range(n):
    ans = 1
    temp = fIn.readline().strip()
    for j in range(1, len(temp)):
        if temp[j] != temp[j - 1]:
            ans += 1
    if temp[-1] == '+':
        ans -= 1
    fOut.write("Case #" + str(T + 1) + ": " + str(ans) + '\n')