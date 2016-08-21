import itertools
import math


def getDivisor(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return i
    return None


def isPrime(num):

    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


def getBinaryNumbers(bits):
    bins = [''.join(x) for x in itertools.product('01', repeat=bits - 2)]
    for i in range(len(bins)):
        bins[i] = '1' + bins[i] + '1'

    return bins


def main():
    # nums_8 = getBinaryNumbers(8)
    nums_16 = getBinaryNumbers(16)
    # nums_32 = getBinaryNumbers(32)

    count = 0
    print "Case #1:"
    for num in nums_16:
        valid = True
        output = [num]
        for base in range(2, 11, 1):
            number = int(num, base)
            if isPrime(number):
                valid = False
                break
            output.append(getDivisor(number))
        if valid:
            count += 1
            print " ".join(map(str, output))

        if count >= 50:
            break
    return

if __name__ == "__main__":
    main()
