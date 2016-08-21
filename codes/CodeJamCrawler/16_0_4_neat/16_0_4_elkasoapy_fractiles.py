#!/usr/bin/env python

################################################################################
#
# Google Code Jam 2016 - Qualification round
#
# Problem D - Fractiles
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
        problem_list.append([int(n) for n in current_line.strip().split(' ')])

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def solve_fractiles(k, c, s):
    original_k_positions = range(1,k+1)
    k_combinations = [original_k_positions[i:i+c] for i in xrange(0, len(original_k_positions), c)]

    if s < len(k_combinations):
        return 'IMPOSSIBLE'

    check = []

    for combination in k_combinations:
        for index, position in enumerate(combination):
            if index == 0:
                check_position = position
            else:
                check_position += (position-1) * k**index

        check.append(str(check_position))

    return ' '.join(check)


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python fractiles.py <input_file> <output_file>'
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
        solution = solve_fractiles(problem[0],problem[1],problem[2])
        line = 'Case #' + str(index + 1) + ': ' + str(solution)
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
