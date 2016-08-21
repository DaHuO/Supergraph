#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from sys import argv

def flip(pancake_stack):
    return pancake_stack.replace('+','X').replace('-','+').replace('X','-')

def happy_side_up(pancake_stack):
    if pancake_stack == "+":
        return 0
    elif pancake_stack == "-":
        return 1
    elif pancake_stack[-1] == "+":
        return happy_side_up(pancake_stack[:-1])
    elif pancake_stack[-1] == "-":
        return 1 + happy_side_up(flip(pancake_stack))

if __name__ == "__main__":
    if len(argv) < 2:
        print "Error\nUsage: " + argv[0] + " input_file.in"
        quit()

    test_cases = open(argv[1], "r").read().split("\n")
    for i in range(1, len(test_cases)): # Skip first line
        pancake_stack = test_cases[i]
        if pancake_stack != '':
            print "Case #" + str(i) + ": " + str(happy_side_up(pancake_stack))
