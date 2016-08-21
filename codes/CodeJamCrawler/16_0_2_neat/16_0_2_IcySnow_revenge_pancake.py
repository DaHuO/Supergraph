'''
Created on Apr 9, 2016

@author: nguyen
'''

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        pass

    with open(sys.argv[1], 'r') as fi:
        with open('revenge_pancake_output.txt', 'w') as fo:
            count = int(fi.readline())
            for i in range(count):
                cakes = fi.readline().strip()
                j = len(cakes) - 1
                while j >= 0 and cakes[j] == '+':
                    j -= 1
                moves = 0
                if j >= 0:
                    moves = 1
                    for idx in range(1, j+1):
                        if cakes[idx] != cakes[idx-1]:
                            moves += 1
                fo.write('Case #%d: %d\n' % (i+1, moves))
    pass