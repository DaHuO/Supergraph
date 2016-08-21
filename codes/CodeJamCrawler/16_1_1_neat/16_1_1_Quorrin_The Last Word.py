f = open('input1.in', 'r')
t = int(f.readline().strip())
out = open('output1.txt', 'w')


for i in range(t):
    inputStr = list(f.readline().strip())
    result = [inputStr[0]]
    for j in range(1, len(inputStr)):
        if (inputStr[j] >= result[0]):
            result.insert(0, inputStr[j])
        else:
            result.append(inputStr[j])

    result = ''.join(result)
    print(result)
    out.write("Case #" + str(i + 1) + ": " + result + "\n")
out.close()
f.close()


