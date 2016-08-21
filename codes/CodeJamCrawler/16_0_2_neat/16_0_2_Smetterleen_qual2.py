'''
Created on Apr 9, 2016

@author: joep
'''
import os

ds_type = 'large'
BASE = os.path.dirname(os.path.realpath(__file__))

inf = open(os.path.join(BASE, 'B-large.in'.format(ds_type)), 'r')
outf = open(os.path.join(BASE, '{}.out'.format(ds_type)), 'w+')

cases = int(inf.readline())

for case in range(cases):
    s = inf.readline().strip()
    
    flips = 0
    l_p = s[0]
    for i, p in enumerate(s):
        if p != l_p:
            flips += 1
            
        l_p = p
    if s[-1] == '-':
        flips += 1
        
    outf.write('Case #{}: {}\n'.format(case + 1, flips))
    print('Finished {}'.format(case + 1))
        
