__author__ = 'okremer'

import sys

def calc_base(arr, base):
    result = 0
    i = 0
    for currNum in reversed(arr):
        currAddition = base**i
        result += int(currNum) * currAddition
        i+=1
    return result

def is_prime(n):
    if n%2 == 0: return 2
    if n%3 == 0: return 3
    r = int(n**0.5)
    f = 5
    while f <= r and f < 500:
        if n%f == 0: return f
        if n%(f+2) == 0: return f+2
        f +=6
    return True

inputFile = open(sys.argv[1], 'r')
outputFile = open("output.txt",'w')

lineCount = inputFile.readline()

for i in range(0,int(lineCount)):
    currLine = inputFile.readline()
    n = int(currLine.split(' ')[0])
    j = int(currLine.split(' ')[1])

    resArray = list()
    k = 1
    start = 2**(n-1)
    end = start + 1000
    outputFile.write("Case #1:\n")
    while (k <= j):
        for currNumber in range(start, start + 1000):
            resArray = list()
            for nn in range(0, 9):
                resArray.append(1)
            flag = True
            arr = list("{0:0b}".format(currNumber))
            if (arr[0] == '0' or arr[-1] == '0'):
                continue
            for base in range(2,11):
                res = is_prime(calc_base(arr,base))
                if (res == True):
                    flag = False
                    break
                else:
                    resArray[base-2] = res
            if flag == True:
                outputFile.write(''.join(arr) + " ")
                for x in resArray:
                    outputFile.write(str(x) + " ")
                outputFile.write("\n")
                k += 1
                if (k > j):
                    break
        start += 1000
