'''
Created on Apr 9, 2016

@author: nguyen
'''

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        pass

    with open(sys.argv[1], 'r') as fi:
        with open('counting_sheep_output.txt', 'w') as fo:
            count = int(fi.readline())
            for i in range(count):
                n = int(fi.readline())
                digits = dict()
                if n == 0:
                    fo.write('Case #%d: INSOMNIA\n' % (i+1))
                else:
                    nn = n
                    while True:
                        digit_str = str(nn)
                        for charidx in range(len(digit_str)):
                            digits[digit_str[charidx]] = 0
                        if len(digits) == 10:
                            fo.write('Case #%d: %d\n' % (i+1, nn))
                            break
                        else:
                            nn += n
    pass