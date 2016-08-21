import sys


def sleep_strategy(n, seen, updated_count, multiplier):
    current = n*multiplier
    digits = [int(x) for x in str(current)]

    for digit in digits:
        if seen[digit]:
            continue

        seen[digit] = True
        updated_count += 1

        if updated_count == 10:
            return current

    return sleep_strategy(n, seen, updated_count, multiplier+1)


def main():
    test_cases_count = sys.stdin.readline().strip()

    for case_no in range(1, int(test_cases_count)+2):
        starting_number = sys.stdin.readline().strip()

        if not starting_number:
            continue
        elif starting_number == '0':
            print 'Case #%s: INSOMNIA' % case_no
            continue

        print 'Case #%s: %s' % (case_no, sleep_strategy(int(starting_number), [False]*10, 0, 1))

if __name__ == '__main__':
    main()
