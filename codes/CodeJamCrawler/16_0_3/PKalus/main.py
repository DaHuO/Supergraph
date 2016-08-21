#!/usr/bin/python

import math
import sys


def getDiviser(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return i
    return None


def convertBase(num, base):
    convert_string = "0123456789"
    if num < base:
        return convert_string[num]
    else:
        return convertBase(num // base, base) + convert_string[num % base]


def incBin(num):
    return convertBase(int(str(num), 2) + 2, 2)

input_file = open(sys.argv[1], "r")
numbers = input_file.read().split()
length = int(numbers[1])
count = int(numbers[2])
divisors = []

f = open('output.out', "w")
f.write("Case #1:\n")

jamcoin = convertBase((2**(length-1))+1, 2)
#print(jamcoin)

i = 1
while i <= int(count):
    divisors.clear()
    for k in range(2, 11):
        div = getDiviser(int(jamcoin, k))
        if div is None:
            jamcoin = incBin(jamcoin)
            break
        divisors.append(div)
    if len(divisors) == 9 and divisors.count(None) == 0:
        f.write(jamcoin)
        for j in range(0, 9):
            f.write(" " + str(divisors[j]))
        f.write("\n")
        i += 1
        jamcoin = incBin(jamcoin)
