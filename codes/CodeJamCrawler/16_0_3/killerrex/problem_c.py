#!/usr/bin/env python3
# coding=utf-8

"""
    Solve Quals 2016 p.C

    Author: killerrex
"""

import sys


class PrimeSet:
    Known = [2, 3, 5, 7]

    @classmethod
    def _is_prime_so_far(cls, n):
        """
        Check if a number is prime, up to the last known prime
        Args:
            n: Number to test
        """
        for p in cls.Known:
            if n % p == 0:
                return False
        return True

    @classmethod
    def _grow(cls):
        """
        Add the next prime to the list
        Returns: The last prime added
        """

        n = cls.Known[-1]
        big = n % 6 == 1
        ok = False
        while not ok:
            # Advance to the next position...
            if big:
                n += 4
            else:
                n += 2
            big = not big
            ok = cls._is_prime_so_far(n)

        cls.Known.append(n)
        return n

    def __contains__(self, item):
        """
        Search a prime in the list
        Args:
            item:
        Returns:
        """
        # Search using a binomial search
        # We know that p[item] > item
        l = 0
        u = min(item, len(self.Known) - 1)
        if self.Known[0] == item or self.Known[u] == item:
            return True

        while u - l > 1:
            m = (l + u) // 2
            p = self.Known[m]
            if p == item:
                return True

            if p > item:
                u = m
            else:
                l = m
        return False

    def __init__(self):
        """
        Create a new iterator in the primes
        """
        super().__init__()

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        yield from self.Known

        # Now we need to grow each time
        while True:
            yield self._grow()


def coinjammify(n, value, desist=100):
    """
    Convert v in a coinjam of n bits
    Args:
        n: Number of bits
        value: initial value

    Returns:
        The coinjam or None
    """
    if n <= 2:
        return None
    # Force to be 1__n-2 bits___1
    tpl = '1{:0{n}b}1'.format(value, n=n-2)

    bases = list(range(2, 11))
    proof = [0]*len(bases)
    # Obtain the number in each base:
    values = [(b, int(tpl, b)) for b in bases]

    patience = desist
    for p in PrimeSet():
        patience -= 1
        sz = len(values)
        # Enumerate in reverse, to be able to pop elements
        for k in range(sz-1, -1, -1):
            b, v = values[k]

            if p >= v:
                # Prime found... this is not a coinjam
                return None, None

            if v % p == 0:
                proof[b-2] = p
                del values[k]
                patience = desist
        if len(values) == 0:
            break
        # Just too long
        if patience <= 0:
            return None, None
    return tpl, proof


def paranoid(tpl, proof):
    for k, p in enumerate(proof):
        b = k + 2
        v = int(tpl, b)
        if v % p != 0:
            return False
    return True


def solve(fd):
    """
    Read the cases from fd and solve them

    Args:
        fd: File descriptor

    Returns:

    """

    total = int(fd.readline().strip())

    for k in range(total):
        n, j = (int(c) for c in fd.readline().strip().split())

        print("Case #{}:".format(k+1))
        v = 0
        vmax = 1 << (n-2)
        t = 0
        # Estimate the patience we must have...
        patience = 2*j
        while v < vmax:
            cj, proof = coinjammify(n, v, patience)
            v += 1
            if cj is None:
                continue
            t += 1

            if not paranoid(cj, proof):
                print("Invalid: {} {}".format(cj, proof))
                raise RuntimeError("This shall not pass")

            proof = ' '.join(str(p) for p in proof)
            print(cj + ' ' + proof)
            if t >= j:
                break
        else:
            print("Not enough patience...")


def start():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fd:
            solve(fd)
    else:
        solve(sys.stdin)

if __name__ == '__main__':
    start()
