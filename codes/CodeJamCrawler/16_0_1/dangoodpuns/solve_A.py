# Problem A for Code Jam 2016
# Dan Elliott
# Run with Python 2.7

#Remember to set these flags to False before submitting
IoDebug = False #Check file input on sample file
solveDebug = False #Run hard-coded test cases
debug = True #print debug lines


runMain = True #turn to False when developing solution

def printToFile(fout,line):
    if debug: print line
    fout.write(line+'\n')

def readInputFile(filename, linesPerTestCase = 1):
    testCases = []
    fin = open(filename)
    lines = fin.read().splitlines()
    fin.close()
    numCases = int(lines[0])
    line = 1
    if debug: print 'numCases',numCases
    for i in range(0,numCases):
        testCase = []
        for j in range(line,line+linesPerTestCase):
            testCase.append(lines[j])
        line += linesPerTestCase
        testCases.append(testCase)
    return testCases

def solve(N):
    if N == 0:
        return (False,0)
    # for non-trivial case
    seen = [0 for i in range(1,11)]
    i = 1
    while i < 2**33: #high condition incase oops
        curNum = i*N
        for d in str(curNum):
            seen[int(d)]+=1
        done = True
        for el in seen:
            if el == 0:
                done = False
        if done:
            return (True,curNum)
        i+=1
    return (False,0)

def main():
    filename = 'A-large.in'
    linesPerTestCase = 1
    testCases = readInputFile(filename,linesPerTestCase)
    fout = open('out.txt','w')
    curTestCase = 1
    for testCase in testCases:
        if debug:
            print 'curTestCase',curTestCase
        N = int(testCase[0])
        result = solve(N) #todo fix
        if result[0] == True:
            printToFile(fout,'Case #'+str(curTestCase)+': '+str(result[1]))
            #print 'Case #'+str(curTestCase)+':',result
        else:
            printToFile(fout,'Case #'+str(curTestCase)+': '+'INSOMNIA')
            #print 'Case #'+str(curTestCase)+':',result
        curTestCase +=1
    fout.close()


## RUN FULL SOLUTION ##
if runMain:
    if debug: print 'run main'
    main()

## TEST EXAMPLE CASES ##
if solveDebug:
    if debug: print 'solve examples'
    print solve(0) # False
    print solve(1) # 10
    print solve(2) # 90
    print solve(11) # 110
    print solve(1692) # 5076

## TEST AREA ##
if IoDebug:
    testCases = readInputFile('sample.txt',2)
    print testCases

