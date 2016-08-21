import sys
from operator import itemgetter
import math
import numpy as np
import copy

def generate(K,C,i):
    #start = []
    start = ''
    bintot = str(bin(i))[2:]
    # pad it to get it to the correct length
    if len(bintot) < K**C:
        bintot = '0'+bintot
    
    curr = bintot
    for c in xrange(0,C-1):
        nextv = ''
        for i in curr:
            if i=='1':
                for k in xrange(0,K):
                    nextv+='1'#[True, True, True]
            else:
                nextv+= start
        print nextv
        curr = copy.deepcopy(nextv)
    return curr

    return bintot
        

def calculate(K,C,S):
    # K is number of tiles at the beginning
    # C is complexity
    # S is number of students
    # look at worst case - only 1 of them is a G, don't know which one
    # however, there is a symmetry - only need to consider the first half of the tiles!
    # pattern to follow:
    '''
    for i in xrange(0,K):
        position = i+1
        #calculate after complexity C
        positions = []
        curr = 0
        while (curr < K**C):
            total+=
    '''
    #for k in range(1,K):
    tiles = []   
    return tiles # didn't find a possible option

infile = open(sys.argv[1],'r')

numcases = int(infile.readline().strip())
outfile = open(sys.argv[1].replace('.in','.out'),'w')
for n in range(numcases):
    #N = int(infile.readline().strip())
    c_i_str = infile.readline().strip().split()
    K = int(c_i_str[0])
    C = int(c_i_str[1])
    S = int(c_i_str[2])
    #print 'getting difference'
    #diff = calculate(K,C,S)
    #print diff
    ans = ''
    outfile.write("Case #" + str(n+1)+":")# + ans + '\n')
    #if diff == -1:
    #    outfile.write(" IMPOSSIBLE\n")
    #else:
    for j in xrange(1,K+1):
        anstmp = j
        outfile.write(" " + str(anstmp))
        ans += ' ' + str(anstmp)
    outfile.write("\n")
    print ans

outfile.close()
