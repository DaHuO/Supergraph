#!/usr/env python3
'''
Created on 2016/04/09

@author: kenji
'''
import sys

def gen_problem(filename):
    with open(filename) as fsp:
        for num, line in enumerate(fsp):
            if num == 0:
                pass
                #case_num = int(line.strip())
            else:
                yield int(line.strip())

def solve_problem(number):
    if number == 0:
        return 'INSOMNIA'
    
    vals = set(range(10))    

    count = 1
    while True:
        n = count * number
        while n > 0:
            n, rem = divmod(n, 10)
            if rem in vals: vals.remove(rem)
        if not vals:
            break
        count += 1
    
    return count * number

def solve_all(filename, ofilename):
    with open(ofilename, 'w') as ofs:
        for num, prob in enumerate(gen_problem(filename), 1):
            answer = solve_problem(prob)
            ofs.write('Case #{0}: {1}\n'.format(num, answer))

if __name__ == '__main__':
    solve_all(sys.argv[1], sys.argv[2]);