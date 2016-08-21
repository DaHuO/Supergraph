import sys

INF = 'INSOMNIA'
ALL_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def last_number(start):
    length = len(str(start))
    cur = start
    digits = []

    if start == 0:
        return INF

    while True:
        cur_digits = list(str(cur))
        digits += cur_digits
        has_all = True

        for d in ALL_DIGITS:
            if not d in digits:
                has_all = False
                break

        if has_all:
            return cur
        
        cur += start

def print_case(case_number, res):
    print("Case #%d: %s" % (case_number, str(res)))

def parse_limits(line):
    return int(line.strip())

def parse_test(line):
    return int(line.strip())

def run():
    # Parse input
    lines = sys.stdin.read().split('\n')
    T = parse_limits(lines[0])
    lines = lines[1:]

    # Run program and get output
    for i in range(0, T):
        start = parse_test(lines[i])
        print_case(i + 1, last_number(start))

if __name__ == '__main__':
    run()
