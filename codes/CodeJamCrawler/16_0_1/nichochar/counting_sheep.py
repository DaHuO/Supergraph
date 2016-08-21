#!usr/local/bin/python
import sys
data = sys.stdin.readlines()

number_of_cases = int(data[0])


def solve_one(start):
    """Returns the last int marked"""
    if start == 0:
        return 'INSOMNIA'
    mult = 1
    length = 0
    digits = {}
    while length != 10:
        current = start * mult
        string_int = str(current)
        for digit in string_int:
            if digits.get(digit) is None:
                length += 1
                digits[digit] = 1
        mult += 1

    return current


for i in xrange(number_of_cases):
    max_hit = solve_one(int(data[i + 1]))
    print "Case #%s: %s" % (i + 1, max_hit)
