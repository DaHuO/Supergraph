#!/usr/bin/python3

import sys


def main():
    with open(sys.argv[1]) as input_file:
        content = [line.strip('\n') for line in input_file.readlines()]

    case_count = int(content[0])

    with open('output', 'w') as output_file:
        for case_number in range(1, case_count + 1):
            case_input = content[case_number]

            # Do computations here
            result = flip_pancakes(case_input)

            output_file.write('Case #' + str(case_number) + ": " + result + '\n')


def flip_pancakes(pancakes):
    flips = 0
    previous = pancakes[0]
    for pancake in pancakes[1:]:
        if previous != pancake:
            flips += 1
        previous = pancake
    if previous == '-':
        flips += 1
    return str(flips)


if __name__ == '__main__':
    main()
