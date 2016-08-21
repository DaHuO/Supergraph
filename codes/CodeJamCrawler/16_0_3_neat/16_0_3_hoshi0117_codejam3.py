#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

# standard module
import os
import sys
import math

# install required

# from local script

class MaybeTakeLongTimeException(Exception):
    pass

class Codejam3Solver:

    def __init__(self, N, J):
        self.N = int(N)
        self.J = int(J)

    def __is_prime(self, number):
        number = abs(number)
        if number == 2:
            return True
        if (number < 2) or (number & 1 == 0):
            return False
        return pow(2, number -1, number) == 1
        
    def __gen_prime(self, limit):
        if limit > 2:
            yield 2

        for value in range(3, int(limit) + 1, 2):
            if self.__is_prime(value):
                yield value

    def __get_first_devisor(self, not_prime_value):
        limit = math.sqrt(not_prime_value)
        for i, prime in enumerate(self.__gen_prime(limit)):
            if not_prime_value % prime == 0:
                return prime
            if i > 10000:
                raise MaybeTakeLongTimeException()

    def __gen_base2to10(self, jamstring):
        return [int(jamstring, n) for n in range(2, 11)]

    def __is_jamcoin(self, jamstring):

        if len(jamstring) < 2:
            return False

        if ((jamstring[0] != '1') or (jamstring[-1] != '1')):
            return False

        for value in self.__gen_base2to10(jamstring):
            if self.__is_prime(value):
                return False
        return True

    def __result_formatter(self, jamcoin):
        divisors = [str(self.__get_first_devisor(value)) for value in self.__gen_base2to10(jamcoin)]
        return "{0} {1}".format(jamcoin, " ".join(divisors))

    def __gen_candidate_length_N(self):
        if self.N == 2:
            yield "11"
        else:
            maxvalue = 2 ** (self.N - 2)
            for value in range(maxvalue):
               var = format(value, 'b').zfill(self.N - 2)
               yield "1" + var + "1"

    def get_answer(self):
        cnt = 0
        for candidate in self.__gen_candidate_length_N():
            if self.__is_jamcoin(candidate):
                try:
                    print(self.__result_formatter(candidate))
                    cnt += 1
                except MaybeTakeLongTimeException:
                    continue

            if cnt >= self.J:
                break

lines = [line.strip() for line in open(sys.argv[1])]
target = lines[1:int(lines[0])+1]
for i, NJ in enumerate(target):
    values = NJ.split(" ")
    print("Case #{0}:".format(i + 1))
    solver = Codejam3Solver(values[0], values[1])
    solver.get_answer()
