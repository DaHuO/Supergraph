import importlib
import sys


def run_data(input_lines, output, process):
    total_cases = int(input_lines.next())
    for i in xrange(1, total_cases + 1):
        output('Case #{0}: {1}'.format(i, process(input_lines.next())))


def stdin_lines():
    while True:
        yield raw_input()


def print_thing(thing):
    print thing


def sample_lines(st):
    for line in st.split('\n'):
        yield line


class OutputCollector(object):
    def __init__(self):
        self.output = ''

    def collect_line(self, line):
        self.output = '%s%s\n' % (self.output, line)


def test(problem):
    sample_output_lines = sample_lines(problem.sample_output)

    def do_one_example(thing):
        return sample_output_lines.next()

    oc = OutputCollector()

    print 'First, make sure testing function works.'
    run_data(
        sample_lines(problem.sample_input),
        oc.collect_line,
        do_one_example
    )
    print oc.output
    assert oc.output == problem.sample_output
    print 'All good!\n'

    oc = OutputCollector()

    print 'Now, test sample input and output.'
    run_data(
        sample_lines(problem.sample_input),
        oc.collect_line,
        problem.do_one
    )
    print oc.output
    assert oc.output == problem.sample_output
    print 'All good!'


def process(problem):
    run_data(
        stdin_lines(),
        print_thing,
        problem.do_one
    )


if __name__ == '__main__':
    problem = importlib.import_module('problem1')
    if '-t' in sys.argv:
        test(problem)
    else:
        process(problem)
