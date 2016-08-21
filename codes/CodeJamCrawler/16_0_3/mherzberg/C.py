import math
N = 32

J = 500

def convert(digits, base):
    res = 0
    for i in range(len(digits) - 1, -1, -1):
        if (digits[i] == 1):
            res += base ** (len(digits) - 1 - i)
    return res

def getDivisor(num):
    #for i in range(2, round(math.sqrt(num)) + 1):
    for i in range(2, 1000):
        if (num % i == 0):
            return i
    return num

def iterateDigits(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 0:
            digits[i] = 1
            break
        else:
            digits[i] = 0
    digits[-1] = 1

digits = [int(x) for x in str((10 ** (N - 1)) + 1)]
print("Case #1:")
for j in range(0, J):
    divisors = []
    while True:
        for base in range(2, 11):
            num = convert(digits, base)
            #print("converting digits " + str("".join([str(i) for i in digits])) + " to base " + str(base) + " is eq to num " + str(num))
            divisor = getDivisor(num)
            if divisor == num:
                break
            divisors.append(divisor)
        if (len(divisors) == 9):
            break
        iterateDigits(digits)
        divisors.clear()
    outstr = "".join([str(i) for i in digits])
    for base in range(2, 11):
        outstr += " " + str(divisors[base - 2])
    print(outstr)
    #print(convert(digits, 10) // divisors[8])
    iterateDigits(digits)
