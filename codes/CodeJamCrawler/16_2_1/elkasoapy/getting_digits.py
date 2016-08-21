#!/usr/bin/env python

################################################################################
#
# Google Code Jam 2016 - Round 1B
#
# Problem A - Getting the Digits
#
# Victoria Lopez Morales - elkasoapy@gmail.com
#
################################################################################

import sys
import os


def read_problem_file(filename):
    problem_list = []

    # Read the file with the input data
    out_file = open(filename, 'r')
    all_file = out_file.readlines()
    out_file.close()

    n_problems = int(all_file.pop(0).strip())

    for current_line in all_file:
        problem_list.append(current_line.strip())

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def getting_phone(input_str):
    digits_conversion = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    first_letter = {'Z': 0, 'W': 2, 'U': 4, 'X': 6, 'G': 8}
    second_letter = {'O': 1, 'H': 3, 'F': 5, 'S': 7}
    third_letter = {'I': 9}
    digits = []

    current_str = {}

    for c in input_str:
        if c in current_str.keys():
            current_str[c] += 1
        else:
            current_str[c] = 1

    # First set of unique identifiers
    for digit in first_letter:
        if digit in current_str:
            for i in range(current_str[digit]):
                digits.append(first_letter[digit])
                for c in digits_conversion[first_letter[digit]]:
                    if current_str[c] > 1:
                        current_str[c] -= 1
                    else:
                        del current_str[c]

    # Second set of unique identifiers
    for digit in second_letter:
        if digit in current_str:
            for i in range(current_str[digit]):
                digits.append(second_letter[digit])
                for c in digits_conversion[second_letter[digit]]:
                    if current_str[c] > 1:
                        current_str[c] -= 1
                    else:
                        del current_str[c]

    # What is left is the nines
    for digit in third_letter:
        if digit in current_str:
            for i in range(current_str[digit]):
                digits.append(third_letter[digit])
                for c in digits_conversion[third_letter[digit]]:
                    if current_str[c] > 1:
                        current_str[c] -= 1
                    else:
                        del current_str[c]

    if len(current_str) > 0:
        print 'Wrong formatted phone!'
        print input_str + ' is not formed of digits'
        sys.exit()

    digits.sort()

    return ''.join([str(d) for d in digits])


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python getting_digits.py <input_file> <output_file>'
        sys.exit()

    problems_file = sys.argv[1]
    if not os.path.isfile(problems_file):
        print 'Incorrect first parameter given to this script: ' + sys.argv[1]
        print 'The given file does not exist'
        sys.exit()

    # Read the input data
    problems_values = read_problem_file(problems_file)

    # Process the problems
    output = []
    for index, problem in enumerate(problems_values):
        solution = getting_phone(problem)
        line = 'Case #' + str(index + 1) + ': ' + str(solution)
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
