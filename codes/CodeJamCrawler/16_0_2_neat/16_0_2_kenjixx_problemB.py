'''
Created on 2016/04/09

@author: kenji
'''
import sys

def gen_problem(filename):
    #convertion = lambda x: True if x == '+' else False
    with open(filename) as fsp:
        for num, line in enumerate(fsp):
            if num == 0:
                pass
                #case_num = int(line.strip())
            else:
                #yield [ convertion(x) for x in reversed(line.strip()) ]
                yield line.strip()
                

blank = '-'
happy = '+'
def cost(pancakes, flip_to = happy):
    #print('{0} flip to {1}'.format(list(pancakes), flip_to))
    if flip_to not in pancakes:
        return 1
    if (blank if flip_to == happy else happy) not in pancakes:
        return 0
    else:
        rev = pancakes[::-1]
        pos = rev.find(happy if pancakes[-1] == blank else blank)
        return 1 + cost(rev[pos:], happy if pancakes[-1] == blank else blank)


def solve_problem(pancakes):
    #return func(pancakes[::-1], purpose=True)
    return cost(pancakes, pancakes[-1]) + (0 if pancakes[-1] == happy else 1)


def solve_all(filename, ofilename):
    with open(ofilename, 'w') as ofs:
        for num, prob in enumerate(gen_problem(filename), 1):
            #print('#{0}: {1}'.format(num, prob)) 
            answer = solve_problem(prob)
            ofs.write('Case #{0}: {1}\n'.format(num, answer))


if __name__ == '__main__':
    solve_all(sys.argv[1], sys.argv[2]);