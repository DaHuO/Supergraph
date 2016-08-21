import time
import math


def isPrime(n):
    for i in [2, 3, 5, 7]:
        if n % i == 0:
            return False
    return True


def value_in_base(base, jamstring):
    total = 0
    place = 0
    reverted_jamstring = jamstring[::-1]
    for c in reverted_jamstring:
        total += int(c) * base ** place
        place += 1
    return total


def is_jamcoin(somestring):
    if somestring.startswith('0') or somestring.endswith('0'):
        return False
    for n in range(2, 11):
        val = value_in_base(n, somestring)
        if isPrime(val):
            return False
    return True


def get_jamcoin_candidate(length, num):
    inner = bin(num)[2:]
    candidate = '1' + '0' * (length - len(inner) - 2) + inner + '1'
    return candidate


def first_divisor(num):
    for i in [2, 3, 5, 7]:
        if num % i == 0:
            return i
    return 0


def get_divisors(jamcoin):
    divisors = ''
    for n in range(2, 11):
        val = value_in_base(n, jamcoin)
        div = first_divisor(val)
        divisors = divisors + ' ' + str(div)
    return divisors


def generate_jamcoins(length, howMany, filehandler):
    cnt = 0
    attempt = 0
    while cnt < howMany:
        candidate = get_jamcoin_candidate(length, attempt)
        attempt += 1
        if is_jamcoin(candidate):
            filehandler.write(str(candidate) + get_divisors(candidate) + '\n')
            print(str(candidate) + get_divisors(candidate))
            cnt += 1


start_time = time.time()

outputFile = open("coins.txt", 'w')

outputFile.write('Case #1:\n')
generate_jamcoins(32, 500, outputFile)

outputFile.close()

print("--- %s seconds ---" % (time.time() - start_time))
