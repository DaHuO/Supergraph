import math

fileIn = open("C-small-attempt0.in", "r")
fileOut = open("c_output.txt", "w")

caseNum = int(fileIn.readline())
fileOut.write("Case #1:\n")

line = fileIn.readline()
digits = int(line.split()[0])
remaining = int(line.split()[1])

def toDec(num, base):
    value = 0
    for i in range(len(num)):
        value *= base
        value += int(num[i])
    return value

def toBin(num):
    return bin(num)[2:]

def zero(digits, num):
    num = toBin(num)
    return (digits - len(num)) * "0"

def isPrime(num):
    sqrt = math.sqrt(num)
    i = 2
    while i <= sqrt:
        if num % i == 0:
            return i
        i += 1
    return -1

def allComposite(bases):
    for i in range(len(bases)):
        if bases[i] == -1:
            return False
    return True

def toString(listy):
    stringy = ""
    for i in listy:
        stringy += str(i) + " "
    return stringy

for i in range(2 ** (digits - 2)):
    coin = "1" + zero(digits - 2, i) + toBin(i) + "1"
    bases = [2,3,4,5,6,7,8,9,10]
    for j in range(len(bases)):
        prime = isPrime(toDec(coin, bases[j]))
        bases[j] = prime
        if prime == -1:
            break
    if allComposite(bases):
        remaining -= 1
        fileOut.write(coin + " " + toString(bases) + "\n")
        print(coin + " " + toString(bases) + "\n")
    if remaining == 0:
        break
if remaining != 0:
    print("rip")
fileIn.close()
fileOut.close()
