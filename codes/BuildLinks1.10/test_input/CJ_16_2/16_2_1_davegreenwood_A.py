from __future__ import division

nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
        "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

keys = [('Z', 0), ('W', 2), ('U', 4), ('R', 3), ('O', 1),
        ('F', 5), ('X', 6), ('S', 7), ('G', 8), ('N', 9)]


def str2list(s):
    return [x for x in s]


def rm_num(c, n, sl, result):
    while c in sl:
        t = rm_char(n, sl)
        if not t:
            break
        result.append(n)


def rm_char(n, sl):
    for c in nums[n]:
        try:
            sl.remove(c)
        except:
            print 'Not in list'
            return False
    return True


def f(s):
    sl = str2list(s)
    result = []
    for (c, n) in keys:
        rm_num(c, n, sl, result)
    return ''.join([str(x) for x in sorted(result)])


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
        case = data[r].strip()
        M.append(case)
        r += 1  # n
    return M


def solve(case):
    '''
    solve individual case
    return solution as string, or single scalar
    '''
    return f(case)


def main():
    infile = 'A-large.in.txt'
    outfile = 'A-out.txt'
    case_list = parse(read(infile))
    write(outfile, case_list)

if __name__ == '__main__':
    main()
