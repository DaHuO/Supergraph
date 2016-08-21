import sys
import random

# converts a list of 1's and 0's interpreted in base i, to base 10 equivalent
def base_i_to_base_10(binary, i):
    return sum([binary[j]*(i**(len(binary)-j-1)) for j in range(len(binary))])

# checks primality of a number
# if prime, return -1
# if composite, return the divisor that indicated so
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return i
    return -1

# Function to check if a number (whose digits are 0 and 1) is prime
# Primality is tested by converting the number into bases 2 through 10
# If prime, we return []; representing that no divisors exist
# If composite, we return a ['some divisor'] as proof
def notPrime(binary):
    theFactors = []
    # iterates over bases 2 through 10
    for i in range(2,11):
        num = base_i_to_base_10(binary, i) # number after converting to base i
        divisor = isPrime(num)
        if divisor==-1:
            return [] # the number was prime in base i
        else:
            theFactors += [divisor] # the number is not prime in base i
    return theFactors # the number is composite in bases 2 through 10

# Reads in how many test cases there are
try:
   caseNums = int(sys.stdin.readline().strip("\n"))
except ValueError:
   pass      # or whatever


case = 0 # initalize case count to zero

# read lines from standard input
for line in sys.stdin:
    case += 1
    # each line contains two numbers
    # N is the number of digits the binary number contains
    # by binary we mean made up of 1's and 0's, and not necessarily in base 2
    # J is the number of binary digits that are not prime in any of the bases
    # 2 through 10 and begin and end with 1, that we would like to generate
    N, J = [int(i) for i in line.strip('\n').split(' ')]

    print "Case #{}:".format(case) # print out test case number

    valid = [] # list of valid binary numbers satisfying the requiremnts
    seen = [] # list of binary numbers we've considered already

    # randomly generate a candidate binary number
    binary = [1]+[int(random.random() > 0.5) for i in range(N-2)]+[1]

    # A list of divisors, one from each base 2 through 10
    # If the number is not prime in atleast one of the above bases, divs = []
    divs = notPrime(binary) 

    # while we haven't generated J many valid binary numbers, keep searching
    while (len(valid)<J):

        # if the randomly generated binary number isn't one we've seen already
        # and if it is prime across all bases 2 through 10
        # record the binary number as valid
        if ( not (binary in seen) and len(divs)==9):
            # dispay binary number and some of its divisors
            num = ''.join([str(i) for i in binary]) + " "
            for i in divs:
                num += str(i)+" "
            num = num.strip(' ')
            print num

            valid += [binary] # mark binary number as valid

        seen += [binary] # mark the binary number as already seen

        # generate a new binary number to consider, and some of its divisors
        binary = [1]+[int(random.random() > 0.5) for i in range(N-2)]+[1]
        divs = notPrime(binary)
