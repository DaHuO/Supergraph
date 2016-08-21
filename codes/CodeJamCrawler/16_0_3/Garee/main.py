#!/usr/bin/env python3

import numpy
import math


# Start: http://codereview.stackexchange.com/questions/67599/convert-between-two-bases-each-between-2-and-36
def base_to_base(starting_base, string, ending_base):
    n = string_to_int(string, starting_base)
    return int_to_string(n, ending_base)


def string_to_int(string, base):
    num = 0
    for digit in string:
        if digit.isalpha():
            current_value = ord(digit) - 55
        else:
            current_value = int(digit)
        num = base * num + current_value
    return num


def int_to_string(n, base):
    if n==0:
        return "0"

    string = ""
    while n:
        n, current_value = divmod(n, base)
        if current_value > 9:
            current_value = chr(current_value + 55)
        else:
            current_value = str(current_value)
        string = current_value + string
    return string


def get_integer_in_range(prompt, mini, maxi):
    while True:
        starting_base = input(prompt)
        if starting_base.isdigit() and mini <= int(starting_base) <= maxi:
            return int(starting_base)
        print("Please enter a positive integer between %d and %d" % (mini, maxi))


def get_starting_num(starting_base):
    """ Input and verification of starting number, that it is a positive integer
    using only characters from its base. Returns starting_num as a string."""
    # Assigns string which only contains characters from the given base
    base_members = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:starting_base]

    while True:
        starting_num = input("starting number: ")
        if all(c in base_members for c in starting_num): 
            return starting_num
        print("Please only use characters in your base (Capital letters for " +
              "bases larger than than 10)")
# END: http://codereview.stackexchange.com/questions/67599/convert-between-two-bases-each-between-2-and-36         


def is_prime_in_bases(n):
    n = numpy.base_repr(n)
    for base in range(2, 11):
        val = int(base_to_base(base, n, 10))
        if is_prime(val):
            return True
    return False


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    k = 3
    while k*k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


def is_jamcoin(n):
    n_str = numpy.base_repr(n)
    digits = set(n_str)
    valid_digits = len(digits) == 2 and "0" in digits and "1" in digits
    valid_first_last_char = n_str[0] == "1" and n_str[-1] == "1"
    return valid_digits and valid_first_last_char and not is_prime_in_bases(n)


def get_divisors(jamcoin):
    divisors = []
    for base in range(2, 11):
        val = int(base_to_base(base, jamcoin, 10))
        divs = divisor_generator(val)
        next(divs)  # Skip 1
        divisors.append(next(divs))
    return divisors


def gen_jamcoins(n, length):
    jamcoins = []
    i = int("1" + ("0" * (length - 2)) + "1", 2)
    while len(jamcoins) < n:
        if is_jamcoin(i):
            jamcoins.append(numpy.base_repr(i))
        i += 2
    return jamcoins


# http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
def divisor_generator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def solve():
    input()  # We already know the number of test cases is 1.
    test_case = input()
    length = int(test_case.split(" ")[0])
    n_jamcoins = int(test_case.split(" ")[1])
    jamcoins = gen_jamcoins(n_jamcoins, length)
    print("Case #1:")    
    for jamcoin in jamcoins:
        divisors = get_divisors(jamcoin)
        print(jamcoin + " ", end="")
        for d in divisors:
            print(str(d) + " ", end="")
        print()


if __name__ == '__main__':
    solve()
