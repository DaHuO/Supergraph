import sys
import fileinput
import math

def answer(ipt):
    length = int(ipt[0])
    s = int(ipt[1])
    start = int(math.pow(2, length-1)) + 1
    end = int(math.pow(2, length))
    for num in range(start, end):
        if s == 0:
            return
        bNum = str(bin(num))[2:]
        factors = check(bNum)
        if factors:
            s -= 1
            factors = [bNum] + factors
            print " ".join(str(f) for f in factors)

def check(bNum):
    lst = []
    for base in range(2, 11):
        num = 0
        power = 0
        if bNum[-1] == '0':
            return None
        for digit in bNum[::-1]:
            num += int(digit) * pow(base, power)
            power += 1
        rst = isPrime(num)
        if rst:
            lst.append(rst)
        else:
            return None
    return lst

def isPrime(num):
    i = 2
    while i * i < num:
        if num % i == 0:
            return i
        i += 1
    return None

inputs  = [line.rstrip() for line in fileinput.input()]
for num in range(1, int(inputs[0])+1):
    print "Case #" + str(num) + ": "
    answer(inputs[num].split())
