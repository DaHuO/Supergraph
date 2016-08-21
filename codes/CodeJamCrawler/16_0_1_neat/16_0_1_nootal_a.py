#!/usr/bin/env pypy
import sys
import os

print(list("10"))

outfile = open("%s.out" % sys.argv[1], "w")

def format_result(index, result):
    return "Case #{}: {}\n".format(index + 1, result)

def solving(index, input):
    if input == 0:
        result = "INSOMNIA"
    else:
        s = set()
        result = input
        while True:
            p = set(list(str(result)))
            s = s.union(p)
            print(s)
            if len(s) == 10:
                break
            result += input

    output = format_result(index, result)
    print(output)
    outfile.write(output)

with open(sys.argv[1]) as infile:
    case = []
    for index, l in enumerate(infile.readlines()[1:]):
        input = int(l.strip())
        solving(index, input)
    
outfile.close()
