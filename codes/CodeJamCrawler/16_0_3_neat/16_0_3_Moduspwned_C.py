#!/usr/bin/env python3
import argparse
import math
import logging



def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        yield f.readline()


def output(n, s):
    outstring = "Case #{}: {}\n".format(n, s)
    print(outstring, end="")
    outfile.write(outstring)


def sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

class PrimeError(Exception):
    pass

def factor(n, primes):
    if n in primes:
        raise PrimeError("PRIME")

    logging.debug("finding factors of {}".format(n))
    for i in primes:
        logging.debug("checking {}".format(i))
        if n % i == 0:
            return i
        if i > math.sqrt(n):
            raise PrimeError("PRIME")
    # At this point it may or may not be prime, but since we dont need
    # perfect results just assume it is
    raise PrimeError("PRIME")


def main():
    for n, case in enumerate(read_input(), start=1):
        logging.info(case)
        N, J = [int(i) for i in case.split()]
        logging.info("N{} J{}".format(N,J))
        biggest = int("1"*N, 9) # This limit is the correct one but we run out of memmory
        # Lets hope we can find ENOUGH results with a subset of primes that we can reasonably compute
        biggest = int("1"*12, 9)
        print(biggest)
        limit = int(math.sqrt(biggest))+1
        print(limit)
        primes = list(sieve(limit))
        logging.info("found all the primes")
        print(max(primes))
        jamcoins = {}
        for i in range(2**(N-2)):
            middle = ("{0:b}".format(i).zfill(N-2))
            s = "1{}1".format(middle)
            print(s)
            factors = []
            try:
                for base in range(2,11):
                    print(base, int(s,base))
                    f = factor(int(s,base), primes)
                    factors.append(f)
            except PrimeError:
                logging.info("{} is prime in a base".format(s))
                # exit(-1)
                continue
            jamcoins[s] = factors
            if len(jamcoins) == J:
                break
            print(jamcoins)
            # exit(-1)
            # number = int('0b1{}1')
        print(jamcoins)
        outstring = ""
        for k,v in jamcoins.items():
            outstring += "\n{} {}".format(k," ".join(str(s) for s in v))
        output(n, outstring)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="google code jam qual 2016")
    parser.add_argument("inputfile", type=str, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    outfile = open(args.inputfile + ".out", "w")
    if args.verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        logging.debug("Verbose debuging mode activated")
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


    # print(fermatfactor(211))
    # print(fermatfactor(221))
    # print(fermatfactor(1000000010011001)) # should give 311
    # exit(-1)
    main()
