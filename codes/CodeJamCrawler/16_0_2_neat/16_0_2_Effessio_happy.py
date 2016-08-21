# coding: utf-8


def rotate(line):
    if set(line) == set("-"):
        return '+' * len(line)
    first = line[0]
    opposite = '-' if first == '+' else '+'
    beg, rest = opposite*line.index(opposite), line[line.index(opposite):]
    return beg + rest


def resolve(case_num, input_stack, num_turns):
    if set(input_stack) == set('+'):
        print "Case #{}: {}".format(case_num, num_turns)
        return
    return resolve(case_num, rotate(input_stack), num_turns + 1)


t = int(raw_input())
for i in xrange(1, t + 1):
    initial = raw_input()
    resolve(i, initial, 0)
