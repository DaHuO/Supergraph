'''
Created on Apr 9, 2016

@author: joep
'''
import os

ds_type = 'large'
BASE = os.path.dirname(os.path.realpath(__file__))

inf = open(os.path.join(BASE, 'A-large.in'.format(ds_type)), 'r')
outf = open(os.path.join(BASE, '{}.out'.format(ds_type)), 'w+')

cases = int(inf.readline())

for case in range(cases):
    n = int(inf.readline())
    
    if n == 0:
        c_n = 'INSOMNIA'
    
    else:
        i = 1
        digs = set()
        while True:
            c_n = str(i * n)
            digs.update(set(c_n))
            
            done = True
            for dig in '0123456789':
                if dig not in digs:
                    done = False
                    break
                
            if done:
                break
            
            i += 1
    
    outf.write('Case #{}: {}\n'.format(case + 1, c_n))
    print('Finished {}'.format(case + 1))
        
