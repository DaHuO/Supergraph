import sys
import re
from random import randint
import random


def parse(s):
    s = s.split()
    s = list(map(int, s))
    return s


def isprime(number):
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False
    oddPartOfNumber = number - 1

    timesTwoDividNumber = 0

    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber / 2
        timesTwoDividNumber = timesTwoDividNumber + 1

    for time in range(3):

        while True:
            randomNumber = random.randint(2, number) - 1
            if randomNumber != 0 and randomNumber != 1:
                break

        randomNumberWithPower = pow(
            int(randomNumber), int(oddPartOfNumber), int(number))

        if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1

            while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):

                randomNumberWithPower = pow(randomNumberWithPower, 2, number)

                # inc the number of iteration
                iterationNumber = iterationNumber + 1
            if (randomNumberWithPower != (number - 1)):
                return False

    return True


def calc(s):
    num = []
    for base in range(2, 11):
        cnum = int(s, base)
        if(isprime(cnum) == True):
            return num
        else:
            i = 2
            while i * i <= cnum:
                i += 1
                if cnum % i == 0:
                    num.append(i)
                    break
                if i > 2000:
                    break
    return num

n = 32
j = 0
nums = []
f = open("output.out", "w+")
f.write("Case #1: \n")

while j < 500:
    s = "1"
    for i in range(n - 2):
        s += str(randint(0, 1))

    s += "1"

    if s not in nums:
        num = calc(s)
        if(len(num) == 9):
            f.write(s + " ")
            f.write(" ".join([str(i) for i in num]))
            f.write("\n")
            nums.append(s)
            j += 1
