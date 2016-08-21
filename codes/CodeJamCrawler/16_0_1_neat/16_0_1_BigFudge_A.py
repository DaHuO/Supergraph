#!/usr/bin/env python

def read_stdin_lines():
    import fileinput
    return [line for line in fileinput.input()]

def parse_lines(lines):
    return [int(l) for l in lines[1:]]

def solve(inputs):
    import itertools
    N = inputs
    if N == 0:
        return "INSOMNIA"
    digits = set()
    for N in itertools.count(N, N):
        digits |= set(list(str(N)))
        if len(digits) == 10:
            assert digits == set(map(str, range(10)))
            return N
        assert digits != set(map(str, range(10)))
        assert digits <= set(map(str, range(10)))


def print_outputs(outputs):
    for n, output in enumerate(outputs):
        print "Case #{}: {}".format(n+1, output)

if __name__ == '__main__':
    lines = read_stdin_lines()
    inputs = parse_lines(lines)
    outputs = map(solve, inputs)
    print_outputs(outputs)
