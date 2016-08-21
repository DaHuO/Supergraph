import os
os.chdir('/Users/mac/OneDrive/competitions/codejam 2016/round2_b/puzzle')
import numpy as np
import math

##extra_need
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_indx = {x:i for i,x in enumerate(alphabet)}

def getb(s):
    b = [0 for _ in alphabet]
    for c in s:
        b[alphabet_indx[c]] += 1
    return b


def geta():
    map = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    a = [[0 for _ in map] for _ in alphabet]
    for i,t in enumerate(map):
        for c in t:
            a[alphabet_indx[c]][i] += 1
    return a

A = geta()

def getW(s):
    B = getb(s)
    x = np.linalg.lstsq(A, B)[0]
    x = [int(abs((round(y)))) for y in x]
    s = ''
    for i,j in enumerate(x):
        s += str(i)*j
    return s
        


##read test.in
test_f = open('./tests/A-large.in.txt')
out_f = open('./tests/A-large.out.txt', 'w+')
test_num = None
test_case_num = 1
current_rcs = []
for line in test_f:
    if test_num == None:
        test_num = int(line)
    else:
        if 
        s = line.strip()
        T = getW(s)
        #print '{}, {}, {}'.format(max_s, audiences, extra_need) 
        out_f.write('Case #{}: {}\n'.format(test_case_num, T))
        test_case_num += 1
        
test_f.close()
out_f.close()