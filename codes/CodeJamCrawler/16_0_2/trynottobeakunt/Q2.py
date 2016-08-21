import sys


def toggle(pancake):
    if pancake == '+':
        pancake = '-'
    elif pancake == '-':
        pancake = '+'
    return pancake


def flip(pancakes, count):
    pancakes = pancakes[::-1]
    for i, pancake in enumerate(pancakes):
        pancakes[i] = toggle(pancake)
    return pancakes, count + 1


def optimise(pancakes):
    flag = pancakes[0]
    count = 0
    pancakes = list(pancakes)
    for i, pancake in enumerate(pancakes):
        if pancake != flag:
            pancakes[:i], count = flip(pancakes[:i], count)
            flag = toggle(flag)

    if flag == '-':
        pancakes, count = flip(pancakes, count)
    return count


filename = sys.argv[1]
t_array = []
out_file = open(filename.replace('in', 'out'), 'w')
with open(filename, 'r') as in_file:
    for line in in_file:
        line = line.rstrip('\n')
        t_array.append(line)
        if len(t_array) > 1:
            result = optimise(line)
            out_file.write("Case #{0}: {1}\n".format(len(t_array) - 1, result))
