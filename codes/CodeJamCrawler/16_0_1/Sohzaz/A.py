#!/usr/bin/python3


import sys

lines = []

with open(sys.argv[1]) as f:
    for line in f:
        lines.append(line.strip())

lines.pop(0)
for index, l in enumerate(lines, start=1):
    if int(l) != 0:
        seen = {'0':False,'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False}
        mul = 1
        val = l
        while False in seen.values():
            for key, value in seen.items():
                if key in val:
                    if not value :
                        seen[key] = True
            if False in seen.values() :
                mul += 1
                val = str(int(l) * mul)
        print("Case #" + str(index) + ":", val)

    
    else:
        print("Case #" + str(index) + ": INSOMNIA")

