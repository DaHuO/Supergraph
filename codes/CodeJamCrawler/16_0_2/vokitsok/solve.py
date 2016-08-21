import sys
import re


def print_result(case_num, result):
    print 'Case #{0}: {1}'.format(case_num, result)


def handle_case(case_num):
    signs = sys.stdin.readline().strip()
    result = 0
    for i in range(1, len(signs)):
        if signs[i] != signs[i - 1]:
            result += 1
    if signs[-1] == '-':
        result += 1
    print_result(case_num, result)


def main():
    T = int(sys.stdin.readline().strip())
    for case_num in xrange(1, T+1):
        handle_case(case_num)


if __name__ == '__main__':
    main()