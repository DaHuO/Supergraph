

import sys
import random
import math
from itertools import count, islice


in_filename = 'example.in'
#in_filename = 'B-small-attempt0.in'
#in_filename = 'A-large-practice.in'
#in_filename = 'B-large.in'

out_filename = 'example.out'
#out_filename = 'B-small-attempt0.out'
#out_filename = 'A-large-practice.out'
#out_filename = 'B-large.out'


def is_prime(n):
    if n == 2:
        return True, 0
    if n % 2 == 0 or n <= 1:
        return False, 2

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False, divisor
    return True, 0

def check_jamcoin(num_str):
    divisors = []
    for i in range(2, 11): # base 2 ~ 10
        num = int(num_str, i)
        prime, divisor = is_prime(num)

        #print "  base={:2} {} {}".format(i, num, prime)
        if prime:
            return False, divisors

        divisors.append(divisor)

        # if prime:
        #     print "{0} {1} {2} {3}".format(num_str, i, num, 'prime')
        #     return False, []
        # else:
        #     divisor = check_prime(num)
        #     print "{0} base={1} value={2} divisor={3}".format(num_str, i, num, divisor)
        #     divisors.append(divisor)

    return True, divisors


def generate_jamcoin(N, J):
    global out_file

    max_array = []
    for i in range(0, N - 2):
        max_array.append('1')
    maxstr = ''.join(max_array)
    max = int(maxstr, 2)
    print "max={}".format(max)

    count = 0
    for i in range(0, max + 1):
        #print "{0:b}".format(i).zfill(N - 2)
        word = "1{}1".format("{0:b}".format(i).zfill(N - 2))
        print "value={}".format(word)

        ret, divisors = check_jamcoin(word)
        if ret:
            divisors_str = []
            for s in divisors:
                divisors_str.append(str(s))
            #print divisors_str
            count += 1
            print "    result[{0}]={1} {2}".format(count, word, ' '.join(divisors_str))

            out_msg = "{0} {1}".format(word, ' '.join(divisors_str))
            out_file.write(out_msg + "\n")

        if count == J:
            break


#num_str = '100011'
#num_str = '110111'
#num_str = '111111'
#num_str = '111001'
#check_jamcoin(num_str)
#generate_jamcoin(6, 3)
#generate_jamcoin(16, 50)

#sys.exit(0)


in_file = open(in_filename, 'r')
out_file = open(out_filename, 'w')

################################################################################
# number of case
line = in_file.readline()
num_of_cases = int(line)
case_index = 1

print "Total Case: " + str(num_of_cases)

while True:
    line = in_file.readline()
    if not line:
        break
    ################################################################################

    tokens = line.strip().split(' ')
    N = int(tokens[0])
    J = int(tokens[1])

    ################################################################################
    out_msg = "Case #{0}:".format(case_index)
    print out_msg
    out_file.write(out_msg + "\n")
    case_index += 1

    ################################################################################
    generate_jamcoin(N, J)


in_file.close()
out_file.close()
