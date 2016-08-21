def fractiles(k, c, s):
    i = 0
    result = [1]
    while 1==1:
        i = i + pow(k, c-1)
        if i >= pow(k,c):
            break
        result.append(i+1)       
    return result

##print fractiles(2,3,2)
##print fractiles(1,1,1)
##print fractiles(2,1,2)
##print fractiles(3,2,3)
    

readFile = open("D-small-attempt0.in")
writeFile = open("D-small-attempt0.out", "a")

numberOfTestCases = -1
caseNumber = 1
for line in readFile.readlines():
    if(numberOfTestCases == -1):
        numberOfTestCases = int(line)
        continue
    #print line
    k,c,s = line.split()
    result = map(lambda x: str(x), fractiles(int(k), int(c), int(s)))
    writeFile.write("Case #" + str(caseNumber) + ": " + (" ").join(result) + "\n")
    caseNumber = caseNumber + 1

readFile.close()
writeFile.close()

