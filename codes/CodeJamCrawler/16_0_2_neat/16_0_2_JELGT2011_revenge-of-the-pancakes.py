
import sys


def revenge_of_the_pancakes(pancakes):
    prev_pancake = pancakes[0]
    flips = 0

    for pancake in pancakes[1:]:
        if pancake != prev_pancake:
            flips += 1
            prev_pancake = pancake

    if not pancakes[-1]:
        flips += 1

    return flips


input_file_path = 'B-large.in'
output_file_path = 'B-large.out'
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:

    T = int(input_file.readline())
    for t in range(1, T + 1):
        line = input_file.readline().splitlines()[0]
        pancakes = [pancake == '+' for pancake in line]
        result = revenge_of_the_pancakes(pancakes)
        output_file.writelines('Case #{0}: {1}\n'.format(t, result))
