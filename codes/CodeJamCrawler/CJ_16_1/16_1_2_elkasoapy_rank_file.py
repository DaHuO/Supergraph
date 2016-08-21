#!/usr/bin/env python

################################################################################
#
# Google Code Jam 2016 - Round 1A
#
# Problem A - The Last Word
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

    n_problems = int(all_file[0].strip())

    n_line = 1
    while n_line < len(all_file):
        # Processing the existing lines
        length_ranks = int(all_file[n_line].strip())
        n_ranks = length_ranks * 2 - 1
        rank_lines = []

        for i in xrange(n_line + 1, n_line + n_ranks + 1):
            rank_lines.append([int(x) for x in all_file[i].strip().split(' ')])

        n_line += (n_ranks + 1)

        problem_list.append((length_ranks, rank_lines))

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def rank_file(n, rank_lines):
    solution = rank_lines[0]

    for line in rank_lines[1:]:
        for number in line:
            if number in solution:
                solution.remove(number)
            else:
                solution.append(number)

    solution.sort()

    return ' '.join([str(x) for x in solution])


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python rank_file.py <input_file> <output_file>'
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
        solution = rank_file(problem[0], problem[1])
        line = 'Case #' + str(index + 1) + ': ' + str(solution)
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
