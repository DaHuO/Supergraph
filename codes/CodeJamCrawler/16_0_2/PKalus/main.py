#!/usr/bin/python

import sys


def flipPancakes(pan, num):
    new_pan = ""
    for i in range(num):
        if pan[i] == "+":
            new_pan += "-"
        else:
            new_pan += "+"
    for i in range(num, len(pan)):
        new_pan += pan[i]
    return new_pan

input_file = open(sys.argv[1], "r")
test = int(input_file.readline())

f = open('output.out', "w")


for line in range(test):
    flip_counter = 0
    pancakes = input_file.readline().strip()
    while pancakes != "+"*len(pancakes):
        # find the bottom most - pancake
        for j in reversed(range(len(pancakes))):
            if pancakes[j] == "-":
                flip_counter += 1
                pancakes = flipPancakes(pancakes, j+1)
    f.write("Case #" + str(line+1) + ": " + str(flip_counter) + "\n")

f.close()
