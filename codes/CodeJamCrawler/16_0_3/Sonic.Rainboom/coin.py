import sys
import math


def factor(num):
    for prime in primes:
        if prime > math.sqrt(num):
            return -1
        elif num % prime == 0:
            return prime
    return -1

prime_file = open("primes.txt", 'r')
primes = []
for line in prime_file:
    primes.append(int(line))
prime_file.close()

    
out_file = open("output.txt", 'w')
out_file.write("Case #1:\n")
N = 32
J = 500

addend = 0
count = 0
while(count < J):

    divisors = []
    fmt = '#0' + str(N) + 'b'
    insert = format(addend, fmt)
    test_num = '1' + insert[2:] + '1'

    divisors.append(factor(int(test_num, 2)))
    if -1 in divisors:
        addend += 1
        continue

    divisors.append(factor(int(test_num, 3)))
    if -1 in divisors:
        addend += 1
        continue

    divisors.append(factor(int(test_num, 4)))
    if -1 in divisors:
        addend += 1
        continue

    divisors.append(factor(int(test_num, 5)))
    if -1 in divisors:
        addend += 1
        continue

    divisors.append(factor(int(test_num, 6)))
    if -1 in divisors:
        addend += 1
        continue

    divisors.append(factor(int(test_num, 7)))
    if -1 in divisors:
        addend += 1
        continue

    divisors.append(factor(int(test_num, 8)))
    if -1 in divisors:
        addend += 1
        continue

    divisors.append(factor(int(test_num, 9)))
    if -1 in divisors:
        addend += 1
        continue

    divisors.append(factor(int(test_num, 10)))
    if -1 in divisors:
        addend += 1
        continue

    answer = test_num  + " " + str(divisors[0]) + \
             " " + str(divisors[1]) + \
             " " + str(divisors[2]) + \
             " " + str(divisors[3]) + \
             " " + str(divisors[4]) + \
             " " + str(divisors[5]) + \
             " " + str(divisors[6]) + \
             " " + str(divisors[7]) + \
             " " + str(divisors[8]) + "\n"
    #sys.stdout.write(answer)
    out_file.write(answer)
    addend += 1
    count += 1


out_file.close()

