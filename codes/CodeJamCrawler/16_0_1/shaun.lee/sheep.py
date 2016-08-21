from __future__ import print_function
import sys


def read_input(in_file):
    T = int(in_file.readline().strip())
    result = [int(line.strip()) for line in in_file]
    return result


def toggle(state):
    if state == "-":
        return "+"
    else:
        return "-"


def check_case(N):
    result = 0
    if N == 0:
        result = "INSOMNIA"
    else:
        k = 0
        seen = set()
        while len(seen) < 10:
            k += 1
            for d in str(k * N):
                seen.add(d)
        result = k * N
    return str(result)


def main():
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            print("Case #" + str(case_no) + ": " + check_case(case))

if __name__ == '__main__':
    main()
