#!/usr/bin/python


import sys


def get_digits(n):
    a = []
    while n > 0:
        a.append(n % 10)
        n = n / 10

    return a

def calc_answer(N):
    curr_N = N
    set_seen = set()
    if N == 0:
        return 'INSOMNIA'
    else:
        while True:
            set_seen.update(get_digits(curr_N))
            if len(set_seen) == 10:
                return str(curr_N)
            curr_N += N



T = 0
curr_T = 0
T = int(sys.stdin.readline().strip())
for curr_T in range(1, T+1):
    N = int(sys.stdin.readline().strip())
    #curr_T += 1
    curr_ans = calc_answer(N)
    print 'Case #%d: %s' % (curr_T, curr_ans)


assert curr_T == T


