# Zolmeister

import sys

fout = open(sys.argv[0] + '.out', 'w')

def pp(t, s):
    out = 'Case #{}: {}'.format(t + 1, s)
    print out
    fout.write(out + '\n')



T = int(input())

for t in xrange(T):
    N = int(input())
    n = N
    seen_digits = set()

    max_rounds = 1000000
    current_round = 0

    while current_round < max_rounds:
        current_round += 1
        for digit in str(n):
            seen_digits.add(digit)

        if len(seen_digits) is 10:
            pp(t, n)
            break

        n += N
    else:
        pp(t, 'INSOMNIA')





fout.close()
