#!/usr/bin/env python3

import sys

def main():
    output = []
    i = 1
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    for line in lines[1:]:
        a = jam(line)
        output.append('Case #{}:\n{}\n'.format(i, a))
        i += 1
    with open('output.txt', 'w') as f:
        for o in output:
            f.write(o)

def jam(tc):
    wallet = []
    div = []
    A = tc.split()
    coin = ['1'] * int(A[0])
    # generate list of prime numbers < 2^16
    primes = prime_primes()
    # run for each desired jamcoin
    for i in range(int(A[1])):
        done = False
        # run until jamcoin found
        while not done:
            div = [''.join(coin)]
            # for each base from 2-10
            for j in range(9):
                # convert to decimal from current base
                test = int(''.join(coin), j + 2)
                div.append(get_div(primes, test))
                # stop if test is prime
                if not div[-1]:
                    break
            else:
                # jamcoin found
                done = True
            # prepare the next coin
            for k in range(len(coin) - 2):
                if coin[k + 1] == '0':
                    coin[k + 1] = '1'
                else:
                    coin[k + 1] = '0'
                    break
        # add jamcoin and proof to wallet
        wallet.append(' '.join(div))
    return '\n'.join(wallet)

def prime_primes():
    primes = [2]
    for i in range(2**15 - 1):
        for p in primes:
            if (i * 2 + 3) % p == 0:
                break
        else:
            primes.append(i * 2 + 3)
    return primes

def get_div(primes, test):
    for i in primes:
        if test % i == 0:
            return str(i)
    return 0

if __name__ == "__main__":
    main()
