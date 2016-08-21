from math import sqrt; from itertools import count, islice

f = open("input.in")
fw = open("output.txt", 'w+')

testCases = 0

first_line = f.readline()
testCases = int(first_line)

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def base_encode(number, base):
    """Convert number in given base to equivalent in base10

    @param number: string, value to convert (case-insensitive)
    @param base:   integer, numeric base of strNumber

    @retval: integer, x base(10) == number base(base)
    """
    # sanitize inputs
    number = str(number).lower()
    base = int(base)

    # legal characters
    known_digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    value  = { ch:val for val,ch in enumerate(known_digits) if val<base }

    # handle negative values
    if number[0]=='-':
        sign = -1
        number = number[1:]
    else:
        sign = 1

    # do conversion
    total = 0
    for d in number:
        try:
            total = total*base + value[d]
        except KeyError:
            if d in known_digits:
                raise ValueError("invalid digit '{0}' in base {1}".format(d, base))
            else:
                raise ValueError("value of digit {0} is unknown".format(d))

    return sign*total

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

for x in xrange(0, testCases):

    n = 0
    j = 0
    jamCoinCount = 0

    line = f.readline()
    numbers = line.split()
    n = int(numbers[0])
    j = int(numbers[1])

    fw.write('Case #{}:\n'.format(x + 1))

    mJamCoin = [] # array to hold the jam
    mJamCoin.append(1)
    for i in xrange(2, n):
        mJamCoin.append(0)
    mJamCoin.append(1)

    for i in xrange(0, 2**(n-2)):
        binaryNo = int(baseN(i, 2))
        padIndex = 2
        while binaryNo:
            digit = binaryNo % 10
            mJamCoin[n - padIndex] = digit
            binaryNo = binaryNo / 10
            padIndex += 1
            pass

        jamNumber = int(''.join(str(v) for v in mJamCoin))

        isValidJamCoin = True
        # mJamCoin have a random jam no; check if prime
        for i in xrange(2, 11):
            convertedNum = base_encode(jamNumber, i)
            if isPrime(convertedNum):
                isValidJamCoin = False
                break
            pass
        pass

        if isValidJamCoin:
            jamCoinCount += 1
            fw.write('{}'.format(jamNumber))

            for i in xrange(2, 11):
                convertedNum = base_encode(jamNumber, i) # in base 10
                nonTrivial = factors(convertedNum)
                for num in nonTrivial:
                    if num != 1 and num != convertedNum:
                        fw.write(' {}'.format(num))
                        break
                    pass
                pass
            fw.write('\n')

        if jamCoinCount >= j:
            print "done"
            break
    pass

f.close()
fw.close()
