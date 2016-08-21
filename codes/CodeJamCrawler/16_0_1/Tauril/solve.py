#!/usr/bin/python2

import sys

nb_cases = 0
N = 0

file_name = sys.argv[1]
file = open(file_name, "r")
content = file.readlines()
file.close()

nb_cases = int(content[0])

def find_digits(storage, number):
    for c in number:
        if storage[int(c)] == 0:
            storage[int(c)] = 1

for i in range (nb_cases):
    N = int(content[i + 1])
    result = str(N)

    stored_digits = [0] * 10

    current_number = list(str(N))

    find_digits(stored_digits, current_number)

    stored = 0
    for j in stored_digits:
        if j == 1:
            stored = stored + 1

    if N != 0:
        multiplier = 1
        n = N
        while stored != 10:
            multiplier = multiplier + 1
            n = N * multiplier
            result = str(n)

            current_number = list(str(n))

            find_digits(stored_digits, current_number)

            stored = 0
            for j in stored_digits:
                if j == 1:
                    stored = stored + 1

    else:
        result = "INSOMNIA"

    print "Case #" + str(i + 1) + ": " + result
