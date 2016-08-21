#!/usr/bin/python


def solve(str_nb, seen_digit, factor):
    nb = int(str_nb)

    for digit in str_nb:
        if digit not in seen_digit:
            seen_digit.append(digit)
            if len(seen_digit) == 10:
                return str_nb
    original_nb = nb / factor
    factor += 1
    new_nb = factor * original_nb
    return solve(str(new_nb), seen_digit, factor)


with open('input.txt', 'r') as input:
    lines = input.read().splitlines()[1:]

    with open('output.txt', 'w') as output:
        for counter, line in enumerate(lines):
            if int(line) == 0:
                solution = 'INSOMNIA'
            else:
                solution = solve(line, [], 1)
            output.write('Case #%s: %s \n' % (counter + 1, solution))
