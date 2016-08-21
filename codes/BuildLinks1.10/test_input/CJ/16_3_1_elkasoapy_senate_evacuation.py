#!/usr/bin/env python

################################################################################
#
# Google Code Jam 2016 - Round 1C
#
# Problem A - Senate Evacuation
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

    n_line = 0
    while n_line < len(all_file):
        # Processing the existing search engines
        n_parties = int(all_file[n_line].strip())
        parties_members = [int(s) for s in all_file[n_line+1].strip().split(' ')]

        n_line += 2

        if n_parties != len(parties_members):
            print 'Wrong formatted file!'
            sys.exit()

        problem_list.append(parties_members)

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def evacuate_senate(senators):
    CHAR_OFFSET = 65
    max = -1
    pos_max = []
    total_senators = sum(senators)
    solution = ''

    while total_senators > 0:
        # Calculate the two majority senators
        max = -1
        pos_max = []
        for i in range(len(senators)):
            if senators[i] > max:
                max = senators[i]
                pos_max = [i]
            elif senators[i] == max:
                pos_max.append(i)

        if total_senators == 2:
            for i in range(min(2,len(pos_max))):
                max = pos_max[i]
                senators[max] -= 1
                total_senators -= 1
                solution += str(unichr(CHAR_OFFSET + max))
        else:
            for i in range(min(2,len(pos_max))):
                if total_senators > 2:
                    max = pos_max[i]
                    senators[max] -= 1
                    total_senators -= 1
                    solution += str(unichr(CHAR_OFFSET + max))
            solution += ' '

    return solution.strip()


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python senate_evacuation.py <input_file> <output_file>'
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
        solution = evacuate_senate(problem)
        line = 'Case #' + str(index + 1) + ': ' + str(solution)
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
