"""
python3 main.py < [input_file]
"""

import sys


def pancakes(x):
    for i in range(len(x) + 1):
        #print("{0}, {1}".format(i,x))
        if all(x):
            return i
        flip_point = (len(x) - 1) - x[::-1].index(False)
        #print("Flippoint={0}".format(flip_point))
        for j, val in enumerate(x[:flip_point+1]):
            #print("Flipping {0}".format(j))
            x[j] = not val


def make_list(x):
    return list(map(lambda s: s == '+', x.rstrip()))


sys.stdin.readline()  # disregard first line. no need to use this count
count = 0
for current_line in sys.stdin:
    count += 1
    boolean_stack = make_list(current_line)
    print("Case #{0}: {1}".format(count, pancakes(boolean_stack)))
