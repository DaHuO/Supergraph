#!/usr/bin/env python

inp = open("A-large.in.txt", 'r')
out = open("large_output.txt", 'w')

ncase = int(inp.readline())

for cidx in range(ncase):
    result = ""
    w = inp.readline()
    w = w.rstrip()
    for c in w:
        if len(result) == 0:
            result = c
            continue
        if ord(result[0]) <= ord(c):
            result = c + result
        else:
            result = result + c

    out.write("Case #" + str(cidx + 1) + ": ")
    out.write(result + '\n')

inp.close()
out.close()
