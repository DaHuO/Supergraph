#!/usr/env python3
'''
Created on 2016/04/09

@author: kenji
'''
import sys
import string
import math
#import numpy as np

def gen_problem(filename):
    with open(filename) as fsp:
        num_parties = 0
        for num, line in enumerate(fsp):
            if num == 0:
                pass
            elif num % 2 == 1:
                num_parties = int(line.strip())
            else:
                prob = [int(x.strip()) for x in line.split()]
                assert(len(prob) == num_parties)
                yield prob 


def get_biggest_and_2nd_biggest(senates):
    s = sorted(senates.items(), key=lambda x:x[1], reverse=True)
    print(s)
    return s[0], s[1]


def check_rule(senates):
    print(senates)
    majority = int((sum(senates.values()) + 2) / 2)
    print('majority: {0}'.format(majority))
    for x in senates.values():
        assert(x >= 0)
        assert(x < majority)


def solve_problem(prob):
    num_parties = len(prob)
    parties = string.ascii_uppercase[0:num_parties] 
    senates = {y : x  for x, y in zip(prob, parties)}
    ans = list()

    while sum(senates.values()) > 0:
        fst_p, snd_p = get_biggest_and_2nd_biggest(senates)
        if sum(senates.values()) == 3:
            ans.append(fst_p[0])
            senates[fst_p[0]] -= 1
        else:
            if fst_p[1] - snd_p[1] >= 2:
                ans.append(fst_p[0] * 2)
                senates[fst_p[0]] -= 2
            else:
                ans.append(fst_p[0] + snd_p[0])
                senates[fst_p[0]] -= 1
                senates[snd_p[0]] -= 1
        #check_rule(senates)

    return ans


def solve_all(filename, ofilename):
    with open(ofilename, 'w') as ofs:
        for num, prob in enumerate(gen_problem(filename), 1):
            answer = solve_problem(prob)
            ofs.write('Case #{0}: '.format(num))
            for senate in answer:
                ofs.write('{0} '.format(senate))
            ofs.write('\n')


if __name__ == '__main__':
    solve_all(sys.argv[1], sys.argv[2]);