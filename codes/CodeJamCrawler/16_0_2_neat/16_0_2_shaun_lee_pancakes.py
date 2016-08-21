from __future__ import print_function
import sys


def read_input(in_file):
    N = int(in_file.readline().strip())
    result = [line.strip() for line in in_file]
    return result


def toggle(state):
    if state == "-":
        return "+"
    else:
        return "-"


def check_case(case):
    # are we currently up or down?
    state = case[0]
    flips = 0
    for pos in range(1, len(case)):
        if case[pos] != state:
            flips += 1
            state = toggle(state)
    if state == "-":
        flips += 1
    return str(flips)


def main():
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            print("Case #" + str(case_no) + ": " + check_case(case))

if __name__ == '__main__':
    main()
