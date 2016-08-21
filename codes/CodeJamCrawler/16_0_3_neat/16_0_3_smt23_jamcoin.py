import math

def runSieve(x):
    for i in range(2,int(math.sqrt(len(x)))):
        if x[i] == True:
            for j in range(i*i,len(x),i):
                x[j] = False

def convertToBinary(x):
    bin = ''
    x = int(x)
    while x > 0:
        if x % 2 == 0:
            bin = '0' + bin
        else:
            bin = '1' + bin
        x = x//2

    return bin

def findDivisor(num,k):
    for x in range(2,101):
        if (1.0*num/x == num//x) and (num != k):
            return x

    return -1

def genVals(s):
    vals = []
    s = s[::-1] #reverse the string
    for i in range(2,11):
        exp = 0
        num = 0
        for x in s:
            num = num + int(x)*(i**exp)
            exp = exp + 1

        vals.append(num)

    return vals

# can never have an even number for the base 10 factor

print(convertToBinary(9))
sieveList = [True for x in range(0,65540)]
sieveList[0] = False
sieveList[1] = False
runSieve(sieveList)
print(sieveList[11])

outFile = open('jamcoin' + '.out','w')
outFile.write('Case #1:\n')

coinList = []
count = 1
for x in range(32769,65535+1):
    binVal = convertToBinary(x)
    if binVal[0] == '1' and binVal[-1] == '1': # make sure it meets the criteria
        if sieveList[x] == False:
            testVals = genVals(binVal)
            sFound = [findDivisor(testVals[i-2],i) for i in range(2,11)]
            if not(-1 in sFound):
                outFile.write(binVal)
                for x in sFound:
                    outFile.write(' ' + str(x))
                outFile.write('\n')
                count = count + 1
                if count > 50:
                    break


print('Total count is: ' + str(count-1))
outFile.close()
