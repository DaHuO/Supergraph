import sys
import math
from decimal import *

filename = sys.argv[1]
f = open(filename, 'r')

numCases = int(f.readline())

for t in range(numCases):
    s = f.readline().strip()
    number = ''
    count = {}
    for c in s:
        if c in count:
            count[c] = count[c] + 1            
        else:
            count[c] = 1            
    if 'Z' in count and count['Z'] > 0:
        number = number + '0' * count['Z']
        count['E'] = count['E'] - count['Z']
        count['R'] = count['R'] - count['Z']
        count['O'] = count['O'] - count['Z']
        count['Z'] = 0
    
    if 'W' in count and count['W'] > 0:
        number = number + '2' * count['W']
        count['T'] = count['T'] - count['W']
        count['O'] = count['O'] - count['W']
        count['W'] = 0

    if 'G' in count and count['G'] > 0:
        number = number + '8' * count['G']
        count['E'] = count['E'] - count['G']
        count['I'] = count['I'] - count['G']
        count['H'] = count['H'] - count['G']
        count['T'] = count['T'] - count['G']
        count['G'] = 0

    if 'X' in count and count['X'] > 0:
        number = number + '6' * count['X']
        count['S'] = count['S'] - count['X']
        count['I'] = count['I'] - count['X']
        count['X'] = 0

    if 'H' in count and count['H'] > 0:
        number = number + '3' * count['H']
        count['T'] = count['T'] - count['H']
        count['R'] = count['R'] - count['H']
        count['E'] = count['E'] - count['H']*2
        count['H'] = 0

    if 'R' in count and count['R'] > 0:
        number = number + '4' * count['R']
        count['F'] = count['F'] - count['R']
        count['O'] = count['O'] - count['R']
        count['U'] = count['U'] - count['R']
        count['R'] = 0

    if 'F' in count and count['F'] > 0:
        number = number + '5' * count['F']
        count['I'] = count['I'] - count['F']
        count['V'] = count['V'] - count['F']
        count['E'] = count['E'] - count['F']
        count['F'] = 0

    if 'O' in count and count['O'] > 0:
        number = number + '1' * count['O']
    if 'V' in count and count['V'] > 0:    
        number = number + '7' * count['V']
    if 'I' in count and count['I'] > 0:    
        number = number + '9' * count['I']

    print 'Case #{}: {}'.format(t+1, ''.join(sorted(list(number))))