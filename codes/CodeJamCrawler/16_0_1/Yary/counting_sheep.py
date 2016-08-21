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
    num = int(input_list)
    last_seen = None
    i = 1
    seen = set()
    while len(seen) < 10:
        new_num = num * i
        #print 'num: {}, i: {}, new_num: {}, last_seen: {}, seen: {}'.format(num, i, new_num, last_seen, seen)
        if new_num != last_seen:
            last_seen = new_num
            seen |= int_to_digits(new_num)
        else:
            return 'INSOMNIA'
        i += 1
    return new_num


def int_to_digits(num):
    num = str(num)
    answ = set()
    for s in num:
        answ.add(int(s))
    #print '\tnum: {}, answ: {}'.format(num, answ)
    return answ


if __name__ == '__main__':
    print sys.argv
    solve(sys.argv[1])
