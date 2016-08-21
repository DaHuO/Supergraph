
import sys


def counting_sheep(N):
    M = 1
    digits = set([int(x) for x in str(N)])

    if N == 0:
        return 'INSOMNIA'

    while len(digits) != 10:
        M += 1
        new_digits = set([int(x) for x in str(M * N)])
        digits = digits.union(new_digits)

    return M * N


input_file_path = 'A-large.in'
output_file_path = 'A-large.out'
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:

    T = int(input_file.readline())
    for t in range(1, T + 1):
        N = int(input_file.readline())
        result = counting_sheep(N)
        output_file.writelines('Case #{0}: {1}\n'.format(t, result))
