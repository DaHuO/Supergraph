inputFileName = "C-small-attempt1.in.txt"
outputFileName = "C_result.out.txt"
inputFile = open(inputFileName, 'r')
outputFile = open(outputFileName, 'a')

from math import sqrt

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def is_prime(num):
    if num == 2:
        return 0
    if (num < 2) or (num % 2 == 0):
        return 2
    for i in mrange(3, int(sqrt(num))+1, 2):
        if(num%i == 0):
            return i
    return 0

def calWithBase(numList, base):
    sum = 0
    for i in range(len(numList)):
        if(numList[len(numList)-1-i] == 1):
            sum += pow(base, i)
    return sum

def nextSample(num):
    noOfDigits = len(num)
    for x in range(noOfDigits):
        if(num[noOfDigits-1-x] == 1):
            pass
        else:
            num[noOfDigits-1-x] = 1
            for y in range(noOfDigits-x, noOfDigits-1):
                num[y] = 0
            break
    return num

def solution(noOfDigits, sampleSize):
    sample = [0] * noOfDigits
    sample[0] = sample[noOfDigits-1] = 1

    while(sampleSize > 0):
        output = ""
        while(True):
            output = [''.join(str(x) for x in sample)]
            print "sample number: " + output[0]
            for i in range(2,11):
                sum = calWithBase(sample, i)
                print "num n base: " + str(sum) + ' ' + str(i)
                factor = is_prime(sum)
                if(factor == 0):
                    break
                else:
                    output.append(" " + str(factor))
        
            if(len(output) < 10):
                sample = nextSample(sample)
            else:
                output = ' '.join(output)
                break
        
        output += "\n"
        print "output: " + output
        outputFile.write(output);
        sampleSize -= 1
        sample = nextSample(sample)


# read/write
noOfCase = int(inputFile.readline());
for i in range(1, noOfCase+1):
    input = inputFile.readline()
    print "input: " + input
    output = "Case #" + str(i) + ": " + "\n";
    print output
    outputFile.write(output);
    n = input.split(" ")
    solution(int(n[0]), int(n[1]))




