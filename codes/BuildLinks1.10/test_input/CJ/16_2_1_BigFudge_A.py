#!/usr/bin/env python

from collections import Counter

numbers = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
all_characters = set(''.join(numbers))

def read_stdin_lines():
    import fileinput
    return [line for line in fileinput.input()]

def parse_lines(lines):
    return [line[:-1] for line in lines[1:]]

def under_target(current, target):
    assert len(current) == len(target)
    return all(c <= t for c, t in zip(current, target))

def get_count(letters):
    count = Counter(letters)
    for character in (c for c in all_characters if c not in count.keys()):
        count[character] = 0
    assert set(count.keys()) == all_characters
    return [n for c, n in sorted(count.items(), key=lambda x: x[0])]

def get_solution(idx, current_str, target_count):
    assert under_target(get_count(current_str), target_count)
    try:
        current_num = numbers[idx]
    except IndexError:
        return None
    current_count = 0
    while under_target(get_count(current_str), target_count):
        # print "trying: {}".format(current_str)
        possible_solution = get_solution(idx+1, current_str, target_count)
        if possible_solution:
            # print "solved! {}".format(current_str)
            possible_solution[idx] = current_count
            return possible_solution
        current_str += current_num
        current_count += 1
        if get_count(current_str) == target_count:
            return {idx: current_count}
    # print "failed with: {}".format(current_str)
    return None

def solve(letters):
    # print "\ttrying for: {}".format(letters)
    target = get_count(letters)
    solution = get_solution(0, '', target)
    expanded_solution = [str(n) * solution[n] for n in sorted(solution.keys())]
    return ''.join(expanded_solution)

def print_outputs(outputs):
    for n, output in enumerate(outputs):
        print "Case #{}: {}".format(n+1, output)

if __name__ == '__main__':
    lines = read_stdin_lines()
    inputs = parse_lines(lines)
    outputs = map(solve, inputs)
    print_outputs(outputs)
