#!/usr/bin/env python

import sys
import os



def get_flip_pivot(plate):
    if plate[-1] == '-':
        return len(plate) - 1
    for idx, pie in enumerate(reversed(plate)):
        if pie == '-':
            z = len(plate) + (idx * -1 - 1)
            return z


def optimal_flip(pancake_plate):
    if '-' not in pancake_plate: return 0

    pivot = get_flip_pivot(pancake_plate)
    for idx, pancake in enumerate(pancake_plate):
        if idx <= pivot:
            if pancake_plate[idx] == '-': pancake_plate[idx] = '+'
            else: pancake_plate[idx] = '-'
    return 1 + optimal_flip(pancake_plate)


if __name__ == '__main__':
    
    input = None
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1]) as file:
            input = file.readlines()[1:]
            for idx, case in enumerate(input):
                idx += 1
                count = optimal_flip(list(case))
                print "Case #" + str(idx) + ": " + str(count)
    else:
        x = optimal_flip(list(sys.argv[1]))
        print "Hello: ", x
