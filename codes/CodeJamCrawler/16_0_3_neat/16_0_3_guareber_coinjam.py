# Coin Jam problem 3
"""
A jamcoin is a string of N ≥ 2 digits with the following properties:

Every digit is either 0 or 1.
The first digit is 1 and the last digit is 1.
If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.
Not every string of 0s and 1s is a jamcoin. For example, 101 is not a jamcoin; its interpretation in base 2 is 5, which is prime. But the string 1001 is a jamcoin: in bases 2 through 10, its interpretation is 9, 28, 65, 126, 217, 344, 513, 730, and 1001, respectively, and none of those is prime.

We hear that there may be communities that use jamcoins as a form of currency. When sending someone a jamcoin, it is polite to prove that the jamcoin is legitimate by including a nontrivial divisor of that jamcoin's interpretation in each base from 2 to 10. (A nontrivial divisor for a positive integer K is some positive integer other than 1 or K that evenly divides K.) For convenience, these divisors must be expressed in base 10.

For example, for the jamcoin 1001 mentioned above, a possible set of nontrivial divisors for the base 2 through 10 interpretations of the jamcoin would be: 3, 7, 5, 6, 31, 8, 27, 5, and 77, respectively.

Can you produce J different jamcoins of length N, along with proof that they are legitimate?
"""
import sys
from math import sqrt
from primes import gen_primes

this = sys.modules[__name__]  
this.primes = []

def is_valid(sequence):
    """
    returns True or False if a sequence is a valid jamcoin
    """
    divisors = []
    for i in range(2,11):
        x = change_base(sequence, i)
        div = find_divisor(x)
        if (div == None):
            return False, None
        else:
            #div = sorted(divs)[1]
            divisors.append(div)

    return True, divisors


def find_divisor(n):
    for x in this.primes:
        if n%x == 0:
            return x

    else:
        return None

def change_base(number_string, base):
    return int(number_string, base)


def generate_base_jamcoin(length):
    """
    Generates the smallest possible binary string representation
    of a length sized jamcoin candidate
    """

    base = '1'
    for x in range(length-2):
        base += '0'

    base += '1'

    return base


def next_increment(binary_number):

    ret = bin(int(binary_number, 2) + 1)[2:]
    while (ret[-1] !='1' or ret[0] != '1'):
        ret = bin(int(ret, 2) + 1)[2:]

    return ret


def generate_jamcoins(amount, length):
    """
    generates a base jamcoin and starts permutating its digits
    until it finds length jamcoins
    """
    valid_jamcoins = []
    base = generate_base_jamcoin(length)
    current_candidate = base
    while (len(valid_jamcoins) < amount):
        valid, divisor = is_valid(current_candidate)
        if ( valid == True ):
            valid_jamcoins.append((current_candidate, divisor))
            print(current_candidate + ' ' + str(divisor))

        current_candidate = next_increment(current_candidate)
        if (len(current_candidate) > length):
            print ('not enough solutions found')
            break

    return valid_jamcoins



def load_testcase(filename):

    with open(filename, 'r') as f:
        f.readline()
        testcases = f.readline().rstrip('\n').split()
        return int(testcases[0]), int(testcases[1])

def print_list(list, filename):
    with open(filename, 'w') as rf:
        rf.write('Case #1\n')
        for coin, divs in list:
            rf.write(coin + ' ' + ' '.join(str(x) for x in divs) + '\n')

if __name__ == "__main__":

    length, amount = load_testcase(sys.argv[1])
    max_values = {16: 256, 32: 65536}
    for x in gen_primes():
        if (x > max_values[length]):
            break
        else:
            this.primes.append(x)

    jamcoins = generate_jamcoins(amount, length)

    print_list(jamcoins, sys.argv[1].replace('.in', '.out'))


