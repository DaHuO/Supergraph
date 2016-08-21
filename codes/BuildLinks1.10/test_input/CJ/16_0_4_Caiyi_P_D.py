# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 15:19:30 2016

@author: caiyi
"""


def func1(K,C):
    """
    K: the length of original sequence
    C: complexity
    return K sets, each contains the positions of G tile of the artwork 
    with complexity C of a single-G original sequence
    
    tested, correct!
    """
    
    res = []
    for pos in range(1,K+1):
        Q = set([pos])
        for comp in range(2,C+1):
            tmp = set()
            for i in range(1, K**(comp-1) + 1):
                if i in Q:
                    tmp_set = set(range((i-1)*K+1, i*K+1))
                    #print 'tmp_set', tmp_set
                    tmp= tmp|tmp_set
                else:
                    tmp.add((i-1)*K + pos)
            Q = tmp
            #print Q
        res.append(Q)
    return res

#print func(3,2)
#print func(2,3)    

def func2(sets, N):
    """
    convert a list of sets into a dictionary
    sets: a list of K sets containing the positions of G tile
    K: the length of original sequence
    N: the range of position is from 1 to N
    rtype: a dictionary: key i stores the the index of sets that contains pos i
    """
    D = {}
    K = len(sets)
    for i in range(1, N+1):
        D[i] = set()
        for pos in range(1, K+1):
            if i in sets[pos-1]:
                D[i].add(pos)
    return D
    
def func3(D,S,K,N):
    """
    determine whether S is enough to remove all K sets
    D: the dictionary
    S: the nb of choice
    N: the length of the artwork
    K: the length of the original sequence
    rtype: if possible, return the number of step, else, return "impossible"
    
    """
    assert len(D) == N
    res = []
    
    removed = set() # ind of 
    for i in range(1,S+1):
        # find the pos with the largest set
        pos = 0
        maxlen = 0
        for key in D:
            if len(D[key]) > maxlen:
                maxlen = len(D[key])
                pos = key
        tmp_set = D[pos]
        
        res.append(pos)
        
        # expand the  removed       
        removed = removed | tmp_set
        if len(removed) == K:
            return res
        
        # updated sets at other positions
        for key in D:
            D[key] = D[key] - tmp_set
    
    return 'impossible'
        
def func_small(K,C,S):
    return range(1,K+1)

def write_res(file_name, res):
    with open(file_name,'w') as f:
        res_str = ''
        for i in range(len(res[:-1])):
            res_str += "Case #{}: ".format(i+1)+ str(res[i])+'\n'
        res_str += "Case #{}: ".format(i+2) + str(res[-1])
        f.write(res_str)
        
#para = (3,2,2)      
##(2 3 2)
##(1 1 1)
##(2 1 1)
##(2 1 2)
##(3 2 3)
#K = 2
#C = 3
#S = 2
#sets = func1(K=K,C=C)    
#D = func2(sets, K**C)
#res = func3(D,S=S,K=K,N=K**C)
#print res

with open('D-small-attempt0.in') as f:
    str1 = f.read()
    l = [[int(item) for item in S.split(' ')] for S in str1.strip().split('\n')[1:]]
res_total = []
for para in l:
    print "para", para
        
    K = para[0]
    C = para[1]
    S = para[2]
    res = func_small(K,C,S)
    
#    sets = func1(K=K,C=C)    
#    D = func2(sets, K**C)
#    res = func3(D,S=S,K=K,N=K**C)
    
    
    print 'res', res
    if res == 'impossible':
        res_total.append('impossible')
    else:
        res_total.append(' '.join([str(i) for i in res]))

write_res('res_D_small.txt', res_total)