#!/usr/bin/env python
# encoding: utf-8

"""
counting_sheep.py
 
Created by Shuailong on 2016-04-09.

https://code.google.com/codejam/contest/6254486/dashboard#s=p0

"""

from collections import Counter
def main():
    input_file_name = 'A-large.in.txt'
    output = 'A-large.out.txt'
    ofile = open(output, 'w')
    with open(input_file_name) as ifile:
        T = int(ifile.readline())
        for case in range(T):
            N = int(ifile.readline())
            res = ''
            if N != 0:
                d = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
                i = 1
                while 0 in d.values():
                    res = i * N
                    s = str(res)
                    for j in s: d[j] = 1
                    i += 1
            else:
                res = 'INSOMNIA'
                    
            ofile.write('Case #%s: %s\n'%(case+1, res))
    ofile.close()

# def test():
#     for N in range(1000001):
#         res = ''
#         if N != 0:
#             d = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
#             i = 1
#             while 0 in d.values():
#                 res = i * N
#                 s = str(res)
#                 for j in s: d[j] = 1
#                 i += 1
#         else:
#             res = 'INSOMNIA'
#         print N, res



if __name__ == '__main__':
    main()
    # test()