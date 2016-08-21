import math
import random

def getDivs(number):
    divs = []
    for base in range(2,11):
        baseNumber = int(number, base)
        wasAppended = False
        for i in range(2, int(math.sqrt(baseNumber))+1):
            if baseNumber % i == 0:
                divs.append(i)
                wasAppended = True
                break
            if i > 10000:
                break
        if wasAppended != True:
            return [1]
    return divs

def getRandNumber(length):
    number = "1"
    for i in range(1, length-1):
        number = number + str(random.randint(0,1))
    number = number + "1"
    return number

def main():
    T = int(input(), 10)
   
    for case in range(1, T + 1):
        N, J = input().split()
        N = int(N, 10)
        J = int(J, 10)
        print("Case #", end="")
        print(case, end="")
        print(":\n", end="")
        i = 0
        numbers = set()
        while True:
            number = getRandNumber(N)
            if number in numbers:
                continue
            numbers.add(number)
            divs = getDivs(number)
            if len(divs) == 9:
                print(number, end="")
                for j in range(0, len(divs)):
                    print(" ", end="")
                    print(divs[j], end="")
                print("\n", end="")
                i = i + 1
            if i == J:
                break

if __name__ == "__main__":
    main()