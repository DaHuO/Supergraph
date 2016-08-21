#!/usr/bin/python2

import sys

nb_cases = 0

file_name = sys.argv[1]
file = open(file_name, "r")
content = file.readlines()
file.close()

nb_cases = int(content[0])

for i in range (nb_cases):
    result = ""

    nb_tiles = int(content[i + 1].split()[0])
    complexity = int(content[i + 1].split()[1])
    nb_students = int(content[i + 1].split()[2])

    if nb_tiles == nb_students:
        for j in range(1, nb_students + 1):
            result += ' ' + str(j)
    elif nb_tiles > nb_students:
        result = " IMPOSSIBLE"

    print "Case #" + str(i + 1) + ':' + result
