import fileinput
from math import *
test_file = fileinput.input()
num_tests = int(next(test_file).strip())

def get_divisor(num):
    if 0 == num % 2:
        return 2
    for i in xrange(3, int(ceil(sqrt(num))), 2):
        if 0 == num % i:
            return i
    return 0

def maybe_print_jamcoin(coin):
    divisors = []
    for i in xrange(2, 11):
        div = get_divisor(int(coin, i))
        if 0 == div:
            return False
        else:
            divisors.append(div)
    output = coin + " " + " ".join(str(d) for d in divisors)
    print output
    return True

for i in xrange(num_tests):
    line = next(test_file).strip().split(" ")
    n = int(line[0].strip())
    j = int(line[1].strip())
    print "Case #%d:" % (i + 1)
    max_num_coins = 2 ** (n - 2)
    coins_printed = 0
    for center in xrange(max_num_coins):
        coin = "1" + "{0:b}".format(center).zfill(n - 2) + "1"
        if maybe_print_jamcoin(coin):
            coins_printed += 1
            if j == coins_printed:
                break
