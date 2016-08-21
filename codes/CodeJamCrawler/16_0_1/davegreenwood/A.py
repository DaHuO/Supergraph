
'''
boiler plate to start off codejam problems
Problem B. Infinite House of Pancakes
'''
from __future__ import division


def read(fname):
    '''
    return the input file line for line
    '''
    with open(fname, 'rb') as fid:
        data = fid.readlines()
    return data


def write(fname, case_list):
    with open(fname, 'wb') as fid:
        for i, case in enumerate(case_list):
            msg = 'Case #{}: {}\n'.format(i + 1, solve(case))
            fid.write(msg)


def parse(data):
    '''
    return a list of cases
    '''
    r, M = 1, []
    while r < len(data):
        # largest first
        case = int(data[r])
        M.append(case)
        r += 1  # n
    return M


def f(case):

    if case == 0:
        return 'INSOMNIA'
    seen = set()
    n = 1

    while len(seen) < 10:
        y = case * n
        for x in str(y):
            seen.add(x)
        n += 1
    return y


def solve(case):
    '''
    solve individual case
    return solution as string, or single scalar
    '''
    return f(case)


def main():
    infile = 'A-large.in.txt'
    outfile = 'A-large-out.txt'
    case_list = parse(read(infile))
    write(outfile, case_list)

if __name__ == '__main__':
    main()
