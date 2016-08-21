from __future__ import division, print_function, unicode_literals

import fileinput

def counting_sheep(N):
    '''
    Code Jam 2016, Qualification Round, Problem A
    '''
    digits = set(range(10))
    for i in range(1, int(1e6)):
        number = i*N
        digits.difference_update([int(x) for x in str(number)])
        if not digits:
            return number
    return 'INSOMNIA'

if __name__ == '__main__':
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            continue
        N = int(line)
        index = i
        answer = counting_sheep(N)
        print("Case #{index}: {answer}".format(index=index, answer=answer))
