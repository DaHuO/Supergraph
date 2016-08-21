#!/usr/bin/env python
# encoding: utf-8

"""
coin_jam.py
 
Created by Shuailong on 2016-04-09.

https://code.google.com/codejam/contest/6254486/dashboard#s=p2

"""

from math import sqrt
def is_prime(num):
    '''
    return one of its divisor of num is not a prime. else return -1
    '''
    if num < 2:
        return -1
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return i
    return -1


def main():
    input_file_name = 'C-small-attempt0.in.txt'
    output = 'C-small-attempt0.out.txt'
    ofile = open(output, 'w')
    with open(input_file_name) as ifile:
        T = int(ifile.readline())
        for case in range(T):
            line = ifile.readline().split(' ')
            N = int(line[0])
            J = int(line[1])

            ofile.write('Case #%s:\n'%(case+1))
            count = 0
            s = '1'+'0'*(N-2)+'1'
            while count < J:
                valid = True
                divisor = [0]*9
                for i in range(2, 11):
                    num = int(s, i)
                    div = is_prime(num)
                    if div == -1:
                        valid = False
                        break
                    else:
                        divisor[i-2] = div
                if valid:
                    ofile.write(s)
                    for i in range(9):
                        ofile.write(' ' + str(divisor[i]))
                    count += 1
                    ofile.write('\n')

                middle = "{0:b}".format(int(s[1:-1], 2)+1)
                if len(middle) < N-2:
                    middle = '0'*(N-2-len(middle)) + middle
                s = '1' + middle + '1'
                
    ofile.close()

if __name__ == '__main__':
    main()

