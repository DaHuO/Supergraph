"""
python3 main.py < [input_file]
"""

import string
import sys


MAX_LOOPS = 10 ** 4
VERBOSE = False


def sheep_count(n):
    if n == 0:
        return "INSOMNIA"
    GOAL = set(string.digits)
    seen = set()
    multiplier = 1

    while multiplier < MAX_LOOPS:
        seen = seen | set(str(multiplier * n))
        if seen >= GOAL:
            if VERBOSE:
                return '{0}*{1} = {2}'.format(*map(str, [multiplier, n, multiplier * n]))
            else:
                return multiplier * n
        multiplier += 1
    return "YOU FUCKED UP JON"


sys.stdin.readline()  # disregard first line. no need to use this count
count = 0
for current_line in sys.stdin:
    count += 1
    print("Case #{0}: {1}".format(count, sheep_count(int(current_line))))
