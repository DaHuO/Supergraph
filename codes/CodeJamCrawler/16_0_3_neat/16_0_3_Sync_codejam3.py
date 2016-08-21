import math
import winsound

def readFile(filename):
    info = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            info.append(line)
    return info

def baseInterpret(string, b):
    return int(string, base=b)

def isPrime(num):
    # Faster prime check, and gives up at 1 million
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    if num < 9:
        return True
    if num % 3 == 0:
        return False
    end = math.sqrt(num)
    check = 5
    while check <= end and check < 1000000:
        if num%check == 0 or num%(check+2) == 0:
            return False
        check += 6
    return True
        
def isNotPrime(num):
    prime = isPrime(num)
    if prime:
        return False, None
    else:
        divisor = 2
        while True:
            if num % divisor == 0:
                return True, divisor
            divisor += 1
    #end = int(math.sqrt(num)) + 1
    #divisor = 2
    #result = 1
    #done = False
    #while divisor < end and not done:
    #    if num % divisor == 0:
    #        result = divisor
    #        done = True
    #    else:
    #        divisor += 1
    #return result != 1, result

def makeString(num, size):
    result = "1"
    for i in range(size - 3, -1, -1):
        test = math.pow(2,i)
        if (num//test > 0):
            result += "1"
            num -= test
        else:
            result += "0"
    result += "1"
    return result
    
    
def main():
    filename = "data.txt"
    info = readFile(filename)
    vals = info[1].split()
    N = int(vals[0])
    J = int(vals[1])
    count = 0
    num = 0
    winsound.Beep(700, 500)
    print("Case #1:")
    while count < J:
        string = makeString(num, N)
        bT = [False] * 11
        bD = [0] * 11
        for i in range(2, 11):
            bT[i], bD[i] = isNotPrime(baseInterpret(string, i))
        test = True
        for i in range(2, 11):
            if bT[i] == False:
                test = False
        if test:
            count += 1
            print("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(string, bD[2], bD[3], bD[4], bD[5], bD[6], bD[7], bD[8], bD[9], bD[10]))
        num += 1
    winsound.Beep(700, 500)
        
