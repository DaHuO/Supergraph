#!/usr/bin/env python
# encoding: utf-8

"""
revenge_of_the_pancakes.py
 
Created by Shuailong on 2016-04-09.

https://code.google.com/codejam/contest/6254486/dashboard#s=p1

"""

def solver_neg(stack):
    # turn all to neg
    if stack == '+':
        return 1
    if stack == '-':
        return 0

    if stack[-1] == '+':
        return solver_pos(stack[:-1]) + 1
    else:
        return solver_neg(stack[:-1])


def solver_pos(stack):
    # turn all to +
    if stack == '+':
        return 0
    if stack == '-':
        return 1

    if stack[-1] == '+':
        return solver_pos(stack[:-1])
    else:
        return solver_neg(stack[:-1]) + 1


def main():
    input_file_name = 'B-large.in.txt'
    output = 'B-large.out.txt'
    ofile = open(output, 'w')
    with open(input_file_name) as ifile:
        T = int(ifile.readline())
        for case in range(T):
            stack = ifile.readline()[:-1]
            res = solver_pos(stack)
            ofile.write('Case #%s: %s\n'%(case+1, res))
    ofile.close()

# def test():
#     tests = ['-', '-+', '+-', '+++', '--+-']
#     for t in tests:
#         print solver_pos(t)

if __name__ == '__main__':
    main()
    # test()
    