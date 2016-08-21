#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem C. Coin Jam
# https://code.google.com/codejam/contest/6254486/dashboard#s=p2
#

import sys
import itertools


class Prime:
    primes = [2, 3]

    def __iter__(self):
        # 見つけてある素数
        for p in self.primes:
            yield p

        for n in self._candidate(p + 1):
            for m in self.primes:
                if n % m == 0 and n != m:
                    # 既存の素数で割り切れた
                    break
                if m ** 2 > n:
                    # 割り切れなった → 素数
                    self.addprime(n)
                    yield n
                    break

    @staticmethod
    def _candidate(start):
        for n in itertools.count(max(start / 6, 1) * 6, 6):
            yield n - 1
            yield n + 1

    @classmethod
    def addprime(cls, p):
        if p not in cls.primes:
            cls.primes.append(p)
            cls.primes.sort()

    @classmethod
    def getfactor(cls, value):
        for p in cls():
            if p > 10 * 8:
                # 高速化のため適度に切り上げる
                break
            if p ** 2 > value:
                # pで割り切れなかった > value は素数
                cls.addprime(value)
                break
            if value % p == 0:
                return p
        return None


def solve(N):
    # 2進数ベースで 10...01 から始める
    for n in itertools.count(int('1' + '0' * (N - 2) + '1', 2), 2):
        coin = bin(n)[2:]
        if len(coin) > N:
            break
        # 2進数〜10進数としてのcoin値チェック
        factor = []
        for base in range(2, 10 + 1):
            value = int(coin, base)
            factor.append(Prime.getfactor(value))
            if not factor[-1]:
                # 素数 ⇒ NG
                break
        else:
            yield coin, factor


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        N, J = map(int, IN.readline().strip().split())
        OUT.write('Case #{}:\n'.format(index + 1))
        for count, (coin, factor) in enumerate(solve(N)):
            if count >= J:
                break
            # 検算
            for index, f in enumerate(factor):
                if int(coin, index + 2) % f != 0:
                    raise Exception('ERROR! {} {} base:{}'.format(coin, factor, index + 2))
            OUT.write('{} {}\n'.format(coin, ' '.join(map(str, factor))))


if __name__ == '__main__':
    main(sys.stdin, sys.stdout)
