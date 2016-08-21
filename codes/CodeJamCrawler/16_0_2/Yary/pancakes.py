import sys


def solve(filename):
    input_list = []
    output = []
    f_input = open(filename, 'r')
    with f_input:
        for line in f_input:
            input_list.append(line.strip('\n\r'))
    cases_number = int(input_list[0])
    for case in xrange(0, cases_number):
        solution = solve_single_case(input_list[1 + case])
        output.append('Case #{0}: {1}\n'.format(case + 1, solution))
    f_out = open('output', 'w')
    with f_out:
        for line in output:
            f_out.write(line)


def solve_single_case(input_list):
    last_seen = input_list[0]
    answ = 0
    if len(input_list) == 1:
        if last_seen == '+':
            answ = 0
        else:
            answ = 1
    else:
        for i in xrange(1, len(input_list)):
            curr = input_list[i]
            if last_seen != curr:
                answ += 1
                last_seen = curr
        if last_seen != '+':
            answ += 1
    return answ


def line_to_set(line):
    splitted = line.split(' ')
    numbers = map(int, splitted)
    return set(numbers)

if __name__ == '__main__':
    print sys.argv
    solve(sys.argv[1])
