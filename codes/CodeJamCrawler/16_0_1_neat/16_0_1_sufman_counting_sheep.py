import sys


class InputFileParser(object):
    def __init__(self, filename):
        self.test_cases = []
        with open(filename, 'r') as in_f:
            self.test_case_count = int(in_f.readline())
            for i in xrange(1, self.test_case_count + 1):
                tc = TestCase(i)
                tc.start = int(in_f.readline().strip())
                self.test_cases.append(tc)


class TestCase(object):
    def __init__(self, index):
        self.index = index
        self.start = None
        self.result = None


def digits(number):
    return map(int, str(number))


def count(number):
    seen = set()
    n = 1
    while True:
        current = number * n
        if not current:
            return 'INSOMNIA'
        seen |= set(digits(current))
        if len(seen) >= 10:
            return current
        n += 1


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('input and output file not specified!')

    parser = InputFileParser(sys.argv[1])
    with open(sys.argv[2], 'w') as out_f:
        for tc in parser.test_cases:
            tc.result = count(tc.start)
            print 'Case #{0}: {1}'.format(tc.index, tc.result)
            out_f.write('Case #{0}: {1}\n'.format(tc.index, tc.result))
