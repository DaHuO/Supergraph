import sys

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def countSheep():
    for testCase in range(1, testCases + 1):
        N = int(input())
        if N != 0:
            numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            i = 0
            while 1 in numbers:
                i+=1
                currentNumber = N * i
                while currentNumber != 0:
                    lastDigit = int(currentNumber % 10)
                    numbers[lastDigit] = 0
                    currentNumber = int(currentNumber / 10)
            print("Case #" + str(testCase) + ": " + ("%i" % (i * N)))
        else:
            print("Case #" + str(testCase) + ": INSOMNIA")


countSheep()