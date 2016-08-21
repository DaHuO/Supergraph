#!/usr/bin/python

import sys

def count_sheeps(n):
    
    digits = [False, False, False, False, False, False, False, False, False, False]
    magic_nro = 1
    counter = 1
    prev_result = -1
    insomnia = False

    while not checkCompleted(digits):
        magic_nro = n * counter

        if magic_nro == prev_result:
            insomnia = True 
            break

        checkDigits(digits, magic_nro)
        prev_result = magic_nro
        counter = counter + 1

    if insomnia:
        return "INSOMNIA"
    
    return magic_nro

    
def checkDigits(digits, result):

    while result >= 10:
        digit = result % 10
        digits[digit] = True
        result = result / 10
    digits[result] = True


def checkCompleted(digits):

    for digit in digits:
        if not digit:
            return digit

    return True


if __name__ == "__main__":

    workfile = sys.argv[1]

    infile = open(workfile, 'r')
    infile.readline()
    outfile = open('output.txt', 'w')
    
    counter = 1

    for line in infile:
        outfile.write('Case #{0}: {1}\n'.format(counter, count_sheeps(int(line))))
        counter = counter + 1

    infile.close()
    outfile.close()