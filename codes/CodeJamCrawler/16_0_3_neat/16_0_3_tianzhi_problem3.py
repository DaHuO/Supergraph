
N = "0" * 30
N = "1" + N + "1"

number = 0


import random

_mrpt_num_trials = 5 # number of bases to test


#Source https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Probably_correct_answers
def check_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True # no base tested showed n as composite



def find_factor(number):
    factor = 2
    while (factor < 1000):
        if ( number % factor == 0 ):
            return factor
        #print("Fuck:" + str(number) + " " + str(factor))
        factor += 1

    return False

def check_bases_prime(number):
    factors = ["None"] * 9
    for x in range(2,11):
        #print("Bitch")
        if not check_prime( int(number, x) ):
            #print("Ass")
            factor = find_factor( int(number, x) )
            #print("Shit" + str(factor))

            if factor != False:
                factors[x-2] = factor
                #print(factors[x-2])
            else:
                return False

        else:
            return False

    #print(factors)
    return factors

def next(N):
    n = list(N)
    for c in range(len(n)-2,0,-1):
        #print("Maybe")
        if n[c] == "0":
            n[c] = "1"
            return "".join(n)
        n[c] = "0"

print("Case #1: ")
while (number < 500):
    ans = check_bases_prime(N)
    if ( ans != False ):
        number += 1
        print(N, end=" ")
        for a in ans:
            print(a, end=" ")
        print("")
    N = next(N)
    #print(N)
