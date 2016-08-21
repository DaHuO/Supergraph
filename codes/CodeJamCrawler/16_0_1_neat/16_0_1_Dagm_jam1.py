import sys

inFileName = sys.argv[1]
outFileName = sys.argv[2]

inFile = open(inFileName,'r')
outFile = open(outFileName,'w')

numCases = int(inFile.readline().strip("\n"))
seen = [False for x in range(10)]
caseCount = 0
for line in inFile:
    caseCount += 1
    line = line.strip('\n')
    count = 1
    while sum(seen)!=10 and line!='0':
        num = str(long(line)*count)
        for i in num:
            if not seen[int(i)]:
                seen[int(i)] = True
       
        count += 1
    if line=='0':
        outFile.write("Case #"+str(caseCount)+": INSOMNIA\n")
    else:
        outFile.write("Case #"+str(caseCount)+": "+str(num)+"\n")
    seen = [False for x in range(10)]
        
        

            
