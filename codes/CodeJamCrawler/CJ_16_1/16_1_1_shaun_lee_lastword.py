from __future__ import print_function
import sys


def read_input(in_file):
    T = int(in_file.readline().strip())
    result = [line.strip() for line in in_file]
    return result


def check_case(S):
    result = ""
    for c in S:
        if c + result > result + c:
            result = c + result
        else:
            result += c
    return result


def main():
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            print("Case #" + str(case_no) + ": " + check_case(case))

if __name__ == '__main__':
    main()
