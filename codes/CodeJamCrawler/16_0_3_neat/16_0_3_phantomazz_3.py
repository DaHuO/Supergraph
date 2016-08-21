# -*- coding: utf-8 -*-

import sys
from math import sqrt
from itertools import islice

PRIMES = []


def load_primes():
    with open("primes.txt", "r") as primes_file:
        global PRIMES
        PRIMES = [long(current_prime.strip())
                  for current_prime in primes_file.readlines()]


def load_input_data():
    with open(sys.argv[1], "r") as input_file:
        input_data = input_file.readlines()
        return input_data[1:]


def find_devisor(number):
    upper_range = sqrt(number) + 1
    for i in PRIMES:
        if i > upper_range:
            return 0
        if number % i == 0:
            return i
    return 0


def check_jamcoin(jamcoin):
    if jamcoin[-1] == "0":
        return []

    devisors = []
    for current_base in range(2, 11):
        current_devisor = find_devisor(long(jamcoin, current_base))
        if current_devisor == 0:
            return []
        devisors.append(current_devisor)

    return [str(devisor) for devisor in devisors]


def generate_jamcoin_candidate(jamcoin_lentgh):
    current_jamcoin = "1" + "0" * (jamcoin_lentgh - 2) + "1"
    while current_jamcoin.count("1") != jamcoin_lentgh:
        yield current_jamcoin
        current_jamcoin = "{0:b}".format(long(current_jamcoin, 2) + 1)


def generate_jamcoin_with_proof(jamcoin_lentgh):
    for current_jamcoin in generate_jamcoin_candidate(jamcoin_lentgh):
        check_result = check_jamcoin(current_jamcoin)
        if check_result:
            yield " ".join([current_jamcoin] + check_result)


def solve_case(index, input_case):
    print("Case #{0}:".format(index))
    (jamcoin_length, jamcoin_count) = tuple(input_case.split())
    for result in islice(generate_jamcoin_with_proof(
            long(jamcoin_length)), 0, long(jamcoin_count)):
        print(result)


def solve(input_data):
    for index, input_case in enumerate(input_data):
        solve_case(index + 1, input_case.strip())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Invalid arguments"
        sys.exit
    load_primes()
    solve(load_input_data())
