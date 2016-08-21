# coding=utf-8

import sys

ifile = sys.stdin
ofile = sys.stdout


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def solve(n, c, numbers):

    #print '------------------'
    if n == 0:
        return 'INSOMNIA'

    #print '{} * {}'.format(n, c)
    n_c = n*c
    #print n_c
    #print 'numbers: {}'.format(numbers)
    new_nums = str(n_c)
    for new_num in new_nums:
        if new_num not in numbers:
            numbers.append(new_num)
    #        print 'added {}'.format(new_num)
    #print 'numbers: {}'.format(numbers)

    if len(numbers) == 10:
        return n_c

    return solve(n, c+1, numbers)


T = int(r())
for case in range(1, T+1):
    #print '####### CASE {} ###############'.format(case)
    n = r()
    what = solve(int(n), 1, [])
    w(case, what)


ofile.close


