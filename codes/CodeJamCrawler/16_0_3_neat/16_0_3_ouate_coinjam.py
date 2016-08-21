#!/usr/bin/env python

import os.path, argparse, math, random

# http://stackoverflow.com/questions/18833759/python-prime-number-checker
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def isCoinJam(num):
    if len(set(list(num))) != 2:
        return False
    if num[0] != '1' or num[-1] != '1':
        return False
    return all(not(is_prime(int(num, i))) for i in range(2, 10))

def nonTrivialDivisor(num):
    for i in range(2, num-1):
        if num % i == 0:
            return i

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="File input", required=True)
    parser.add_argument("-o", "--output", help="File output", required=True)
    args = parser.parse_args()

    lines = list(map(lambda x: x, open(args.input, 'r')))
    T = int(lines[0])

    o = open(args.output, 'w')

    for i in range(0, T):
        NJ = lines[i+1].split()
        N = int(NJ[0])
        J = int(NJ[1])

        o.write("Case #{0}:\n".format(i+1))

        coinjams = []
        while len(coinjams) < J:
            coinjam_candidate = '1'+''.join(random.choice('10') for _ in range(N-2))+'1'
            if isCoinJam(coinjam_candidate) and not(coinjam_candidate in coinjams):
                o.write(coinjam_candidate+' ')
                for j in range(2, 10+1):
                    o.write(str(nonTrivialDivisor(int(coinjam_candidate, j)))+' ')
                o.write("\n")
                coinjams.append(coinjam_candidate)
                print("found one : {0}".format(coinjam_candidate))

        o.close()







