'''
Created on April 12, 2014

@author: Lior
'''


def solve(N):
    if N == 0:
        return 'INSOMNIA'
    seen_digits = set()
    i = 0
    while len(seen_digits) != 10:
        i += 1
        seen_digits.update(set(int(d) for d in str(N*i)))
    return N*i


def process_files(in_file, out_file):
    num_of_test_cases = int(in_file.next().strip())
    for test_number in xrange(num_of_test_cases):
        N = int(in_file.next().strip())
        result = solve(N)
        out_file.write('Case #%d: %s\n' % (test_number+1, result))


if __name__ == '__main__':
    import sys, os
    in_file = sys.argv[1]
    out_file = in_file.replace('.in', '.out')
    with open(in_file, 'rb') as in_file:
        with open(out_file, 'wb') as out_file:
            process_files(in_file, out_file)
