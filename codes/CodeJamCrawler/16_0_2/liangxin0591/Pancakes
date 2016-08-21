#!/usr/bin/python

import sys

def maneuver(cake, i):
    cake = list(cake)
    newCake = len(cake) * ['+']
    for j in range(0,len(cake)):
        newCake[j] = cake[j]

    for j in range(0,i):
        if cake[i - 1 - j] == '-':
            newCake[j] = '+'
        else:
            newCake[j] = '-'

    newCake = "".join(newCake)
    return newCake
    
    

# cake is a string
def pancakes(cake):
    conf = {}
    # now the cake is a list
    queue = []
    flips = []
    if cake == len(cake) * '+':
        return 0
    
    queue.append(cake)
    flips.append(0)
    conf[cake] = 1
    
    while (len(queue) > 0):
        cake = queue.pop(0)
        flip = flips.pop(0)
        for i in range(1,len(cake) + 1):
            newCake = maneuver(cake,i)
            if (newCake == len(cake) * '+'):
                return flip + 1
            else:
                if not (conf.has_key(newCake)):
                    conf[newCake] = 1
                    queue.append(newCake)
                    flips.append(flip + 1)
    return -1

if __name__ == "__main__":
    
    t = int(raw_input()) # read a line with single integer
    for i in range(1, t + 1):
        cake = raw_input()
        flip = pancakes(cake)
        print("Case #" + str(i) + ": " + str(flip))
