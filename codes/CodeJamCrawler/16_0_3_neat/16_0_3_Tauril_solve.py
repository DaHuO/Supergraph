#!/usr/bin/python2

import sys
import math

file_name = sys.argv[1]
file = open(file_name, "r")
content = file.readlines()
file.close()

length = int(content[1].split()[0])
number_jamcoins = int(content[1].split()[1])

print "Case #1:"

def check_validity(jamcoin, dividers):
    valid = 1

    number = 0

    for i in range(2, 11):
        iterator = 0
        number = 0
        for j in jamcoin:
            number = number + (int(j) * pow(i, len(jamcoin) - iterator - 1))
            iterator = iterator + 1

        j = 2
        stop = int(math.sqrt(int(math.sqrt(number) + 1)))
        while j <= stop:
            if j == stop:
                valid = 0
                break
            if (number % j) == 0:
                dividers[i - 2] = str(j)
                break
            j += 1

        if valid == 0:
            break

    return valid

def new_jamcoin(jamcoin):
    last_one = 0
    new_one = 0
    right_one = 0

    for j in reversed(range(1, len(jamcoin))):
        if jamcoin[j] == '1' and jamcoin[j - 1] == '0':
            right_one = j
            break

    for j in reversed(range(1, len(jamcoin) - 1)):
        if jamcoin[j] == '1':
            last_one = j

    nb_zeros = 0

    if last_one != 0:
        for j in reversed(range(last_one + 1, len(jamcoin) - 1)):
            if jamcoin[j] == '1':
                new_one = j
            else:
                nb_zeros += 1

    if nb_zeros == 0 and last_one != 1 and last_one != 0:
        for j in reversed(range(last_one, len(jamcoin) - 1)):
            jamcoin[j] = '0'
        jamcoin[last_one - 1] = '1'
    else:
        if last_one == 0:
            jamcoin[len(jamcoin) - 2] = '1'
        elif new_one == 0:
            jamcoin[right_one - 1] = '1'
        elif new_one == last_one + 1:
            jamcoin[new_one] = '0'
            jamcoin[right_one - 1] = '1'
            jamcoin[right_one - 2] = '1'
        else:
            jamcoin[new_one] = '0'
            jamcoin[new_one - 1] = '1'

    return jamcoin

def is_final_jamcoin(jamcoin):
    final = 1
    for j in jamcoin:
        if j == '0':
            final = 0
            break

    return final

used_jamcoins = []

jamcoin = ['0'] * length
jamcoin[0] = '1'
jamcoin[length - 1] = '1'

dividers = ['0'] * 9

for i in range(number_jamcoins):

    valid = 0
    current_jamcoin = 0

    while 1:
        current_jamcoin = int(''.join(jamcoin))
        if current_jamcoin not in used_jamcoins:
            valid = check_validity(jamcoin, dividers)
            if valid != 0:
                used_jamcoins.append(current_jamcoin)
                break

        jamcoin = new_jamcoin(jamcoin)

    print str(current_jamcoin) + ' ' + ' '.join(dividers)
