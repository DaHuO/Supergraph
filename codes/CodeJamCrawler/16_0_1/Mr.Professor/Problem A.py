nums = []
file = open("A-large.in", "r")
newFile = open("output.txt", "w")

def CheckNumbers(n : int):
    if (n == 0):
        return "INSOMNIA"
    
    numSeen = []
    m = 0
    num = n
    while (not len(numSeen) == 10):
        m += 1
        num = n * m
        for k in str(num):
            if (not k in numSeen):
                numSeen.append(k)
    return num

testCases = int(file.readline())
for i in range(testCases):
    s = "Case #{}: {}".format(i + 1, CheckNumbers(int(file.readline())))
    if (not i == testCases - 1):
        s += "\n"
    newFile.write(s)

file.close()
newFile.close()
