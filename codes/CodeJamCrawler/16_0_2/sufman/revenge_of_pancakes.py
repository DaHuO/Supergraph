import sys


class InputFileParser(object):
    def __init__(self, filename):
        self.test_cases = []
        with open(filename, 'r') as in_f:
            self.test_case_count = int(in_f.readline())
            for i in xrange(1, self.test_case_count + 1):
                tc = TestCase(i)
                tc.stack = map(lambda char: char == '+', in_f.readline().strip())
                self.test_cases.append(tc)


class TestCase(object):
    def __init__(self, index):
        self.index = index
        self.stack = []
        self.result = 0


def fully_ordered(stack):
    return all(stack)


def flip(how_many, stack):
    return list(reversed(map(lambda pancake: not pancake, stack[:how_many]))) + stack[how_many:]


def longest_sequence(stack):
    previous = [stack[0]]
    sequence_length = 0
    for item in stack:
        if item == previous[-1]:
            sequence_length += 1
            previous.append(item)
        else:
            break
    return sequence_length


def order(stack):
    flips = 0
    stacks = [stack]
    while True:
        current_stack = stacks[-1]
        if fully_ordered(current_stack):
            return flips
        else:
            stacks.append(flip(longest_sequence(current_stack), current_stack))
            flips += 1


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('input and output file not specified!')

    parser = InputFileParser(sys.argv[1])
    with open(sys.argv[2], 'w') as out_f:
        for tc in parser.test_cases:
            tc.result = order(tc.stack)
            print 'Case #{0}: {1}'.format(tc.index, tc.result)
            out_f.write('Case #{0}: {1}\n'.format(tc.index, tc.result))
