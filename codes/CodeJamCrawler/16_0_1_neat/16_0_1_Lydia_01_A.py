inputFileName = "A-large.in.txt"
outputFileName = "A_result.out.txt"

def solution(n):
    digitList = [0,1,2,3,4,5,6,7,8,9]
    i = 1
    currentNum = n
    for i in range(1, 1000):
        print digitList
        if((currentNum == 0) & digitList.count(0) > 0):
            digitList.remove(0);
            print 'zero removed'
        while(currentNum > 0):
            digit = currentNum%10
            if(digitList.count(digit)>0):
                digitList.remove(digit)
            currentNum /= 10
        if(len(digitList)==0):
            return n*(i-1)
        else:
            currentNum = n * i

    return 'INSOMNIA'

inputFile = open(inputFileName, 'r')
outputFile = open(outputFileName, 'a')

# read/write
n = inputFile.readline();
caseNo = 1;
while(True):
    input = inputFile.readline()
    print "input: " + input
    if(input == ''):
        break
    n = int(input)
    output = "Case #" + str(caseNo) + ": " + str(solution(n)) + "\n";
    print "output: " + output
    outputFile.write(output);
    caseNo += 1



