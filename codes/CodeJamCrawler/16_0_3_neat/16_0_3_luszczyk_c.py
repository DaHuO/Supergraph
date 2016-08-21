from __future__ import print_function


import primefac  # from PyPI
import random
import sys

def read_ints(): return map(int, raw_input().strip().split())


def choose_potential_coin(j):
    return "".join(
        ["1"] + 
        [random.choice(["0", "1"]) for _ in range(j - 2)] + 
        ["1"]
    )


def prove_coin(string):
    proof = []
    for base in range(2, 11):
        number = int(string, base)
        factor = primefac.pollardRho_brent(number)
        if primefac.isprime(number):
            print("wrong number {} base {}: {}".format(
                string, base, number), file=sys.stderr)
            return None
        assert(number % factor == 0)
        assert(not (factor == 1 or factor == number))
        proof.append(factor)
    return proof


def solve(n, j):
    found = set()
    while len(found) < j:
        number = choose_potential_coin(n)
        if number in found:
            continue
        proof = prove_coin(number)
        if proof is None:
            continue
        found.add(number)
        print(" ".join([number] + map(str, proof)))


def main():
    random.seed(345678)
    t, = read_ints()

    for case in range(t):
        print("Case #{}:".format(case + 1))
        n, j = read_ints()
        solve(n, j)



if __name__ == '__main__':
    main()
