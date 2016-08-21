#!/usr/bin/env pypy
import sys
import os

outfile = open("%s.out" % sys.argv[1], "w")

def format_result(index, result):
    return "Case #{}: {}\n".format(index + 1, result)

def solving(index, input):
    mov = 0
    current = ""
    print(input)
    for pancake in input:
        if pancake == "-":
            if current == "":
                mov += 1
            elif current == "+":
                mov += 2
        current = pancake
    print(mov)
    result = mov

    output = format_result(index, result)
    print(output)
    outfile.write(output)

with open(sys.argv[1]) as infile:
    case = []
    for index, l in enumerate(infile.readlines()[1:]):
        input = l.strip()
        solving(index, input)
    
outfile.close()
