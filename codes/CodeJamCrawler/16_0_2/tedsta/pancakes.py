#!/usr/bin/env python3

import sys

def pancake_flips(pancakes):
    flips = 0
    for i in range(1, len(pancakes)):
        if pancakes[i] != pancakes[i-1]:
            flips += 1
    if pancakes[-1] == '-':
        flips += 1
    return flips

def main():
    if len(sys.argv) < 2:
        print("Usage: pancakes.py <file>")
        exit()
    in_file = sys.argv[1]
    with open(in_file) as f:
        cases = int(f.readline())
        for i, line in enumerate(f):
            pancakes = line.strip() # Strip off the newline
            print("Case #%d: %d" % (i+1, pancake_flips(pancakes)))

##########

if __name__ == '__main__':
    main()
