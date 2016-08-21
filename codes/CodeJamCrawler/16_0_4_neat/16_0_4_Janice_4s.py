myInput = open('D-small-attempt3.in', 'r')
myOutput = open('output.txt', 'w')
T = myInput.readline();
case = 0
for data in myInput:
    case += 1
    K, C, S = map(int, data.split())
    if K == 1:
        myOutput.write("Case #%d: 1\n" % (case))
    elif S < (K/C):
        myOutput.write("Case #%d: IMPOSSIBLE\n" % (case))
    else:
        ans = []
        for i in range(K):
            ans.append(str(i + 1))
        myOutput.write("Case #" + str(case) + ": " + ' '.join(ans))
        myOutput.write("\n")
myInput.close()
myOutput.close()
