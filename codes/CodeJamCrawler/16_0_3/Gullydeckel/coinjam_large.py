#!/usr/bin/python3

import getopt
import sys
import math

def check(a, b):

    n = int(a,b)

    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return i
        if i%1000001 == 0:
           print('.', end='')

    # prime
    return 0

# only check up to small factor
def check_optimistic(a, b):
    max_factor = 20
    
    n = int(a,b)

    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, min(int(math.sqrt(n) + 1), max_factor), 2):
        if n % i == 0:
            return i

    # possibly prime
    return 0




def precheck(a):
    # count number of bits
    nbits = sum([int(k) for k in a])

    # even number of bits ensures that this is even in base(3,5,7,9) - div by 2
    # number of bits divisible by 6 ensures divisible by 3 in base 10
    if nbits % 6 == 0:
        return True

    return False

    
if __name__ == "__main__":

    verbose = False
    fname = "input.txt"

    if sys.version_info[0] < 3:
        print("This script requires Python 3. (You are running %d.%d)" % (
            sys.version_info[0], sys.version_info[1])) 
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvf:",
                                   ["verbose","help","input="])
    except getopt.GetoptError as err:
        print (str(err)) 
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"): sys.exit()
        elif o in ("-v", "--verbose"): verbose = True
        elif o in ("-f", "--input"): fname = a
        else: sys.exit()

    f = open(fname, "rt")
    ncases = int(f.readline())

    for c in range(ncases):
        N, J = [int(x) for x in f.readline().split()]

        print("Case #%d:" % (c+1))
        found = 0

        # generate a candidate and prove it
        #a = '111001'

        # lower limit - e.g. '10001' for N = 5
        lower = pow(2,N-1)+1
        upper = pow(2,N)

        for l in range(lower, upper,2):
            a = bin(l)[2:]

            if(not(precheck(a))):
                continue
        
            # function to interpret number in base x and return non-trivial
            # divisor in if not prime
            is_prime = False
            divisors = list()

        
            for base in range(2,11):
                d = check_optimistic(a,base)

                if verbose:
                    print("%s in base %d is %d, divisor = %d"
                          % (a, base, int(a,base),d))

                divisors.append(d)                
                
                if d == 0:
                    is_prime = True
                    break

            if not(is_prime):
                found += 1
                print(a, end=' ')
                for i in divisors:
                    print(i, end=' ')
                print()

            if found == J:
                if verbose:
                    print("found %d coinjams" % J)
                break

                


            
        
                


        

        




