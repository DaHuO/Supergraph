
from math import sqrt


def init(n):
    jamcoin_int = 1 << (n-1) | 1 << 0
    jamcoin = str(bin(jamcoin_int))
    return jamcoin[2:], jamcoin_int


def next_jamcoin(jamcoin_int):
    jamcoin_int += 1
    if not jamcoin_int & 1:
        jamcoin_int += 1
    return jamcoin_int, str(bin(jamcoin_int))[2:]


def interpret_to_ten(jamcoin_str, src_base, dig_num):
    result = 0
    for i in xrange(0, dig_num):
        result +=  int(jamcoin_str[-(i+1)]) * (src_base ** i)
    return result


def find_divisor(num):
    i = 2
    while i <= sqrt(num):
        if num % i is 0:
            return i
        i+=1
    return 0


def print_line(jamcoin, divisors):
    line = jamcoin
    for div in divisors:
        line += " " + str(div)
    print line

t = int(raw_input())
nj = raw_input().split(" ")
n, j = int(nj[0]), int(nj[1])

jamcoin, jamcoin_int = init(n)
jamcoins_num = 0

print "Case #1:"
while True:
    divisors = []
    
    for base in xrange(2, 11):
        divisor = find_divisor( interpret_to_ten(jamcoin, base, n) )
        if not divisor:
            break
        divisors.append(divisor)

    if len(divisors) < 9:
        jamcoin_int, jamcoin = next_jamcoin(jamcoin_int)
        continue
    else:
        jamcoins_num += 1
        print_line(jamcoin, divisors)
        jamcoin_int, jamcoin = next_jamcoin(jamcoin_int)

    if jamcoins_num == j:
        break
