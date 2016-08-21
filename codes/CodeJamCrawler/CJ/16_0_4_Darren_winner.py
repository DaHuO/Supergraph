#!/usr/bin/env python

import shlex

def read_input():
    input = []
    total = -1
    with open('./input.txt') as f:
        input = f.readlines()
        total = int(input.pop(0))

    return (total, input)

def write_results(data):
    write_out = open('./output.txt', 'w')
    counter = 0

    for index, value in enumerate(data):
        line = str(value)
        write_out.write('Case #')
        write_out.write(str(index+1))
        write_out.write(': ')
        write_out.write(line)
        write_out.write('\n')

    write_out.close()

def is_odd(number):
    return number % 2

def assign_students(original_size):
    limit = int(original_size / 2) + (1 if is_odd(original_size) else 0)
    result = []
    increment = original_size - 1
    position = 1

    for i in range(0, limit):
        position = position + increment
        result.append(position)

    return result

def solve_it(original_size, complexity, students):
    if complexity == 1:
        if original_size == students:
            all_columns = [x for x in range(1, students+1)]
            result = map(str, all_columns)
            return ' '.join(result)
    else:
        if (students * 2) >= original_size:
            #enough students to figure it out
            chosen_tiles = assign_students(original_size)
            result = map(str, chosen_tiles)
            return ' '.join(result)

    return 'IMPOSSIBLE'


def determine_solutions(total_cases, input):
    result = []
    for i in range(0, total_cases):
        parameters = shlex.split(input[i])
        k = parameters[0]
        c = parameters[1]
        s = parameters[2]

        answer = solve_it(int(k), int(c), int(s))
        result.append(answer)

    return result

def main():
    test_data = read_input()
    total_cases = test_data[0]
    input_data = test_data[1]

    results = determine_solutions(total_cases, input_data)

    write_results(results)

main()
