#!/usr/bin/env python3

from sys import argv

matrix = [[0 for x in range(10)] for x in range(10)]

def isAsleep(m):
    awake = True
    sleep_count = 0
    for i in range(10):
        sleep_count = sleep_count + m[i][0]
    
    if sleep_count == 10:
        awake = False
    return awake


def displayOutput(case_number, sleep_count):
    if int(sleep_count) > 0:
        print("Case #{0}: {1}".format(case_number, sleep_count))
    else:
        print("Case #{0}: {1}".format(case_number, "INSOMNIA"))


def initMatrix():
    for i in range(10):
        matrix[i][0] = 0

    
if __name__ == "__main__":
    script, filename = argv
    initMatrix()
    
    with open(filename) as txt:
        lines = txt.read().split('\n')
        for case_nbr in range(1, int(lines[0])+1):
            nbr_input = int(lines[case_nbr])
            if nbr_input == 0:
                displayOutput(case_nbr, nbr_input)
            else:
                multiplier = 1
                awake = True
                while awake:
                    number = str(nbr_input * multiplier)
                    for digit in number:
                        matrix[int(digit)][0] = 1
                    awake = isAsleep(matrix)
                    multiplier += 1
                displayOutput(case_nbr, number)
                initMatrix()
    txt.close
