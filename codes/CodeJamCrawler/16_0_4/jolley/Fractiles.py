# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 07:16:45 2016

@author: jo
"""

with open('input', 'r') as f:
    cases = 0
    case = 0
    with open('output', 'w') as fo:
     for line in f: 
        if case == 0:
            cases = int(line)
            case = 1
            
        else:
            fo.write('Case #' + str(case) + ': ')
            case +=1
            numbers = line.split()
            K = int(numbers[0])
            C = int(numbers[1])
            S = int(numbers[2])
            if (C<2):
                if(S<K):
                    fo.write('IMPOSSIBLE\n')
                else:
                    for k in xrange(K):
                        fo.write(str(k+1) + ' ')
                    fo.write('\n')
                continue
            if(K/S)>2:
                fo.write('IMPOSSIBLE\n')
                continue
            if((K/S)==2)&(K%2)>0:
                fo.write('IMPOSSIBLE\n')
                continue
            sequence = []
            for i in xrange(K):
                if(((i*2)*K**(C-1) +(i+1)*2)<K**C):
                    sequence.append((i*2)*K**(C-1) +(i+1)*2)
                    if(i+1)*2>=K:
                        break
                else:
                    sequence.append(K**C)
                    break
            for s in sequence:
                fo.write(str(s) + ' ')
            fo.write('\n')