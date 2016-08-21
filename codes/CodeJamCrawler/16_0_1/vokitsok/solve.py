import sys
import re


def print_result(case_num, result):
    print 'Case #{0}: {1}'.format(case_num, result)


def handle_case(case_num):
    N = int(sys.stdin.readline().strip())
    if N == 0:
        print_result(case_num, 'INSOMNIA')
        return
    digits_seen = set()
    all_digits = set(range(10))
    i = 1
    while True:
        current = N * i
        digits_seen.update(map(int, str(current)))
        if digits_seen == all_digits:
            print_result(case_num, str(current))
            return
        i += 1

def main():
    T = int(sys.stdin.readline().strip())
    for case_num in xrange(1, T+1):
        handle_case(case_num)


if __name__ == '__main__':
    main()