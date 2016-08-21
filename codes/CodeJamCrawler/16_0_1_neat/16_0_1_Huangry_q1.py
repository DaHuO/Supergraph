import math

with open ('A-large (7).in', 'r') as f:
    with open ('q1solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            N = int(f.readline())
            digits = set()
            answer = ''
            if N == 0:
                answer = 'INSOMNIA'
            else:
                i = 0
                while len(digits) < 10:
                    i += 1
                    N_mult = i*N
                    [digits.add(digit) for digit in str(N_mult)]
                    if len(digits) == 10:
                        answer = str(N_mult)

            solution.write('Case #' + str(case+1) + ': ' + answer + '\n')

        solution.closed
    f.closed