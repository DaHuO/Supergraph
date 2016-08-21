outFile = "output.out"
inFile = "A-large.in"

def allinset(s):
    for i in range(10):
        if not i in s:
            return False
    return True

def calcnum(f, caseNum, t, n):
    worked = False
    digits = set()
    for i in range(1, t+1):
        curNum = n*i
        for char in str(curNum):
            digits.add(int(char))
        if allinset(digits):
            f.write("Case #" + str(caseNum) + ": " + str(curNum) + "\n")
            worked = True
            break

    if not worked:
        f.write("Case #" + str(caseNum) + ": INSOMNIA\n")


with open(inFile, "r") as f:
    with open(outFile, "w") as of:
        t = int(f.readline())
        content = [int(x.strip('\n')) for x in f.readlines()]
        for i in range(0, len(content)):
            calcnum(of, i+1, t, content[i])
