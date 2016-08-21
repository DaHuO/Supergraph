#!/usr/bin/env python3

import sys


def get_file_content(f):
    with open(f, 'r') as input_file:
        return input_file.read()


def rotate_pancakes(pancakes):
    count = 0 
    in_minus = False
    if pancakes[0] == '-':
        count += 1
        in_minus = True

    for i in pancakes[1:]:
        if not in_minus and i == '-':
            count += 2
        if i == '+':
            in_minus = False
        else:
            in_minus = True
        
    return count

def main(argc, argv):
    if argc < 2:
        print("Hey man, give me some file.")
        sys.exit(1)

    numbers = get_file_content(argv[1]).split()
    # 1 <= T <= 100
    for i, pancakes in enumerate(numbers[1:], 1):
        n = rotate_pancakes(pancakes)
        print("Case #{}: {}".format(i, n))
    


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
