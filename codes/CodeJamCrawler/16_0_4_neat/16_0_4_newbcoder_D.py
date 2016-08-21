#!/usr/bin/python

import sys

def solve(K, C, S):
    num = K**C
    #print('K = {:}, C = {:}, S = {:}, K^C = {:}'.format(K,C,S,num))
    return ' '.join(map(str, list(range(num-K+1, num+1))))
        

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        cases = int(f.readline())
        for case in range(cases):
            K, C, S = map(int, f.readline().split())
            ans = solve(K,C,S)
            print("Case #{:}: {:}".format(case+1, ans))


