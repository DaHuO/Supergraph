#!/usr/bin/python
__author__ = 'diogo'

T = int(raw_input())

for case in range(1, T+1):
    N = long(raw_input())
    multiplier = 1
    limit_multiplier = 1
    found = False
    found_array = [False for x in range(0,10)]
    while not found:
        number = str(multiplier * N)
        number_array = [int(x) for x in number]
        for index in number_array:
            if not found_array[index]:
                found_array[index] = True
                limit_multiplier = 10*multiplier
        found = reduce(lambda x,y: x & y, found_array)
        if found:
            print 'Case #'+str(case)+': '+number
        elif multiplier == limit_multiplier:
            print 'Case #'+str(case)+': INSOMNIA'
            found = True
        else:
            multiplier = multiplier+1



