#!/usr/bin/python2

import sys

nb_cases = 0
N = 0

file_name = sys.argv[1]
file = open(file_name, "r")
content = file.readlines()
file.close()

nb_cases = int(content[0])

for i in range (nb_cases):
    number_maneuver = 0
    pancakes = content[i + 1]
    pancakes_list = list(pancakes)

    blank_faces = 0
    for p in pancakes_list:
        if p == '-':
            blank_faces = blank_faces + 1

    if blank_faces != 0:
        while blank_faces != 0:
            to_flip = 0
            first_pancake = pancakes_list[0]

            for p in pancakes_list:
                if p == first_pancake:
                    to_flip = to_flip + 1
                else:
                    break

            for j in range(to_flip):
                if pancakes_list[j] == '-':
                    pancakes_list[j] = '+'
                else:
                    pancakes_list[j] = '-'

            blank_faces = 0
            for p in pancakes_list:
                if p == '-':
                    blank_faces = blank_faces + 1

            number_maneuver = number_maneuver + 1

    print "Case #" + str(i + 1) + ": " + str(number_maneuver)
