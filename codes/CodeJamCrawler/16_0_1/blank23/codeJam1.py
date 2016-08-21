f = open('A-large.in', 'r')
g = open('output.txt', 'w')
inputs = []
for line in f:
    inputs.append(int(line))

def decomposeNum(num):
    arr = []
    strNum = str(num)
    for digit in strNum:
        arr.append(digit)
    return arr

testCases = inputs[0]
for caseNum in xrange(testCases):
    n = inputs[caseNum+1]
    
    result = "INSOMNIA"
    if n > 0:
        s = set()
        i = 0
        currNum = n
        while len(s) < 10:
            i += 1
            currNum = i*n
            digits = decomposeNum(currNum)
            for digit in digits:
                s.add(digit)
        result = currNum
    g.write("Case #" + str(caseNum+1) + ": " + str(result) + "\n")
    
f.close()
g.close()