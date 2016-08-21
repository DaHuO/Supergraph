'''
Created on 2016/04/09

@author: kenji
'''
import sys
import math

class Problem:
    def __init__(self, vals):
        self.K = vals[0]
        self.C = vals[1]
        self.S = vals[2]
    def __repr__(self):
        return "K, C, S = {0} {1} {2}".format(self.K, self.C, self.S)


def gen_problem(filename):
    with open(filename) as fsp:
        for num, line in enumerate(fsp):
            if num == 0:
                pass
                #case_num = int(line.strip())
            else:
                yield Problem([int(x) for x in line.strip().split()])


def solve_problem_small(prob):
    assert(prob.K == prob.S)
    return tuple(range(prob.C, prob.K + 1))


def group_pos(first, last, C, K):
    #print ("first, last = {first} {last} {C} ".format(**locals()))
    if first == last or C == 1: return last
    return K ** (C-1) * (first - 1) + group_pos(first + 1, last, C - 1, K)


def solve_problem(prob):
    if prob.S >= math.ceil(prob.K/prob.C):
        if prob.C == 1: return tuple(range(prob.C, prob.K + 1))
        ans = list()
        count = 0
        #print ("{0}:".format(prob))
        while count < prob.K:
            #print (" {0}".format(count))
            ans.append(group_pos(count + 1,
                                 count + prob.C if count + prob.C <= prob.K else prob.K,
                                 prob.C, prob.K) 
                       )
            count += prob.C
        return ans
    else:
        return None # IMPOSSIBLE


def solve_all(filename, ofilename, solver = solve_problem):
    with open(ofilename, 'w') as ofs:
        for num, prob in enumerate(gen_problem(filename), 1):
            answer = solver(prob)
            if answer:
                ofs.write('Case #{0}:'.format(num))
                for a in answer: ofs.write(' {0}'.format(a))
                ofs.write('\n')
            else:
                ofs.write('Case #{0}: {1}\n'.format(num, 'IMPOSSIBLE'))

if __name__ == '__main__':
    solve_all(sys.argv[1], sys.argv[2], solve_problem);
    #solve_all(sys.argv[1], sys.argv[2]);