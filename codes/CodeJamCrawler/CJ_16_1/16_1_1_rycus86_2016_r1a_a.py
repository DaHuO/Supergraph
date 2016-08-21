__author__ = 'rycus'

# Problem A: The Last Word

FILENAME = 'res/2016_r1a_a.large'
OUTPUT_FILE = '%s.out' % FILENAME


def solve(source):
    current_max = 0
    target = []

    for c in source:
        o = ord(c)

        if o >= current_max:
            current_max = o
            target.insert(0, c)

        else:
            target.append(c)

    return ''.join(target)


if __name__ == '__main__':
    with open(FILENAME) as input_file:
        with open(OUTPUT_FILE, 'w') as output_file:
            num_cases = int(input_file.readline())
            print 'Solving %d test cases' % num_cases

            for case in xrange(1, num_cases + 1):
                S = input_file.readline().strip()
                result = solve(S)

                print 'Case #%d: %s' % (case, result)
                print >> output_file, 'Case #%d: %s' % (case, result)
