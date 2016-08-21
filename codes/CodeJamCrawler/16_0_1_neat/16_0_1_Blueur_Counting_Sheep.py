import sys

inputFile = sys.argv[1]

f = open(inputFile, 'r')

args = f.readline()
T = int(args)

def getDigits(number):
    s = str(number)
    ss = list(s)
    return [int(se) for se in ss]

def answer(n):
    digits = set()
    numbers = set()
    i = 1
    while True:
        c = i*n
        if c in numbers:
            return "INSOMNIA"
        ds = getDigits(c)
        for d in ds:
            digits.add(d)
        if len(digits) == 10:
            return c
        numbers.add(c)
        i = i+1

for t in range(T):
    n = int(f.readline())
    print("Case #{0}: {1}".format(t+1, answer(n)))