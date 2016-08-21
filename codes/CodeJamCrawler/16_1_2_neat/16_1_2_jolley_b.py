# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:13:52 2016

@author: jo
"""
import numpy as np
  

with open('input', 'r') as f:
    with open('output', 'w') as fo:
        cases = int(f.readline())
        print cases
        for case in xrange(1,cases+1):
            fo.write('Case #' + str(case) + ':')
            print('Case: ' + str(case))
    
            N = int(f.readline().strip())
            randc = []
            grid = np.zeros((N,N))
            for n in xrange(2*N-1):
              s = map(int, f.readline().strip().split())
              randc.append(s)
            randc = np.asarray(randc)
            randc = np.sort(randc, axis=0)
            
            occurances = {}
            for a in randc:
                for n in a:
                    if(n in occurances.keys()):
                        occurances[n] = occurances.get(n) + 1
                    else:
                        occurances[n] = 1
            print occurances
            output = []
            for n in occurances.keys():
                print occurances[n]
                if  occurances[n]%2 != 0:
                    output.append(n)
            output.sort()
            if(len(output)> N):
                print 'oops'
            print output
            for n in output:
                fo.write(' ' + str(n))
                       
            fo.write('\n')