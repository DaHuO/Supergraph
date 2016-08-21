#!/usr/bin/python

import sys

numbers = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

unique_sets = [ [('Z',0), ('W',2), ('U',4), ('X',6), ('G',8)], [('O',1), ('H',3), ('F',5), ('S',7)], [('N',9), ] ]


T = int(sys.stdin.readline())

for i in range(0,T):
    strs = sys.stdin.readline().strip()
    number = []
    for unique in unique_sets:
        for c, num in unique:
            while c in strs:
                for cx in numbers[num]:
                    strs = strs.replace(cx, '', 1)
                number.append(str(num))
    print ("Case #"+str(i+1)+": "+''.join(sorted(number)))
