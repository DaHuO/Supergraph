stepsByLen = {1:{"+":0, "-":1}}
prevSteps = stepsByLen[1]

def recurse(pancakes):
    if pancakes == "+":
        return 0
    if pancakes == "-":
        return 1

    if pancakes[-1] == "+" or pancakes[-2] == "-":
        return recurse(pancakes[:-1])

    if pancakes[-2] == "+":
        return 2+recurse(pancakes[:-1])

    print("Weird...")
    input()

inFile = open("B-large.in")
inFile.readline()

outFile = open("B-large.out", "w")

caseNum = 1

for line in inFile:
    orig = line.rstrip()

    length = len(orig)
    print("Case #" + str(caseNum) + ":", recurse(orig), file=outFile)
        
    caseNum += 1

outFile.close()
