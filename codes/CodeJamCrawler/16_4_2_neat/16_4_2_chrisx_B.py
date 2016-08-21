from itertools import zip_longest

def parse(input_file, output_file):
    with open(input_file) as f:
        T = int(f.readline().split()[0])
        out = open(output_file, 'w')
        for i in range(T):
            N, K = map(int, f.readline().split())
            ps = list(map(float, f.readline().split()))
            sol = solve(N, K, ps)
            line = "Case #"+str(i+1)+": "+str(sol)
            print(line)
            out.write(line+'\n')
    return

import itertools

def tie_p(k, kps):
    res = 0
    #perms = itertools.permutations([0]*(k//2)+[1]*(k//2))
    li = list(range(k))
    perms = itertools.combinations(li, k//2)
    for perm in perms:
        prod = 1
        for i in range(k):
            if i in perm:
                prod *= kps[i]
            else: # perm[i] == 0:
                prod *= 1-kps[i]
        res += prod
    return res



def solve(N, K, ps):
    #sortps = sorted(ps)
    #best_p =sortps[0:(K//2)]
    #worst_p = sortps[-(K//2):]
    #return tie_p(K, best_p+worst_p)
    committees = itertools.combinations(ps, K)
    maxx = -1
    for committee in committees:
        maxx = max(maxx, tie_p(K, committee))
    return maxx





dir = "./"

input_file = dir+"B-test.txt"
output_file = dir+"B-test.out.txt"

input_file = dir+"B-small-attempt0.in"
output_file = dir+"B-small-attempt0.txt"

input_file = dir+"B-small-attempt1.in"
output_file = dir+"B-small-attempt1.txt"

input_file = dir+"B-small-attempt2.in"
output_file = dir+"B-small-attempt2.txt"
'''
input_file = dir+"B-large.in"
output_file = dir+"B-large.txt"
'''

parse(input_file, output_file)



