#!/usr/local/bin/python

in_file = open("A-large.in.txt", 'r').readlines()
out_file = open("out.txt", 'wb')


def add_digits(number, digit_set):
    while number != 0:
        digit_set.add(number % 10)
        number = number / 10

for case, number in enumerate(in_file):
    number = int(number)
    if case != 0:
        seen = set()
        if number == 0:
            out_file.write('Case #' + str(case) + ': INSOMNIA\n')
        else:
            i = 1
            while len(seen) < 10:
                add_digits(number * i, seen)
                i += 1
            out_file.write('Case #' + str(case) + ': ' + str(number * (i - 1)) + '\n')

out_file.close()
