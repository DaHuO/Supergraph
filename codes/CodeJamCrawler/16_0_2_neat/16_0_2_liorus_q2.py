'''
Created on April 12, 2014

@author: Lior
'''


def solve(pancakes):
    pancakes = pancakes.rstrip('+')
    if not pancakes:
        return 0
    result = 1
    prev = pancakes[0]
    for c in pancakes[1:]:
        if c == prev:
            continue
        result += 1
        prev = c
    return result


def process_files(in_file, out_file):
    num_of_test_cases = int(in_file.next().strip())
    for test_number in xrange(num_of_test_cases):
        pancakes = in_file.next().strip()
        result = solve(pancakes)
        out_file.write('Case #%d: %s\n' % (test_number+1, result))


if __name__ == '__main__':
    import sys, os
    in_file = sys.argv[1]
    out_file = in_file.replace('.in', '.out')
    with open(in_file, 'rb') as in_file:
        with open(out_file, 'wb') as out_file:
            process_files(in_file, out_file)
