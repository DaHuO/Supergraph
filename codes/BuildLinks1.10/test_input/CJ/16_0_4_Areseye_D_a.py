#encoding:utf8
import os
import pdb


def solve(K,C,S):
    ret = [1,]
    gap = K**(C-1)
    cur = 1
    for i in range(0,K-1):
        cur += gap
        ret.append(cur)
    return ret;

if __name__ == '__main__':
    with open('d.in','r') as fin:
        for ind,line in enumerate(fin):
            if ind is 0:
                T = int(line)
            else:
                strnum = line.split(' ')
                param = map(int,strnum)
                res = solve(*param)
                resstr = map(str,res)
                print 'Case #{}: {}'.format(ind,' '.join(resstr))

