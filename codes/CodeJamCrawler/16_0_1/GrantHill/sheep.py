#!/usr/bin/python3

import sys;

def add_digits(number, digits):
    while number > 0:
        digits.add(number % 10)
        number = number // 10

def have_all_digits(digits):
    return digits == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


def get_last_number(number):
#    import pdb; pdb.set_trace()
    digits = set()
    counter = number
    lastNumber = number
    while True:
        add_digits(counter, digits)
        if have_all_digits(digits):
            return counter
        lastNumber = counter
        counter += number
        if lastNumber == counter:
            return "INSOMNIA"


        
if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
        numCases = int(infile.readline())
        for i in range(1, numCases+1):
            print("Case #{}: {}".format(i, get_last_number(int(infile.readline()))))
