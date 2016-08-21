# -*- coding: utf-8 -*-
"""
 
@author: Luca
"""

# General imports
#import numpy as np
#import scipy as sc
#import itertools
import sys

def read_word(f):
    return next(f).strip()

def read_int(f, b=10):
    return int(read_word(f), b)

def read_letters(f):
    return list(read_word(f))

def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
    return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]

def read_arr(f, R, reader=read_ints, *args, **kwargs):
    return [reader(f, *args, **kwargs) for i in range(R)]


    
def main_reader(T,f):
    N,J= read_ints(f)
    return {'T':T,'N':N,'J':J}    


def naive_solver(T,N=None,J=None):
# Create sequence of jam coin of length N
   print 'Case #1:'   
   results = []
   results_str = []
   fmt_str='{0:0%db}'%(N-2)
   for i in xrange((2**(N-2))):
       #print i
       jc = '1%s1'%(fmt_str.format(i))
# Test JC
       
       #jc = '110111'
       #print jc
       divisor = [0]*9
       for b in range(2,11):
           value_b = long(jc,b)
           #print 'value base %d: %d'%(b,value_b)
           for d in xrange(2,min([int(1e6),value_b/2])):
               if value_b%d==0:
                   divisor[b-2]=d
                   #print divisor
                   break
       if min(divisor)>0:
           results.append((jc,divisor))
           div_str = [str(t) for t in divisor]
           results_str.append('%s %s'%(jc,' '.join((div_str))))
           print results_str[-1]
       if len(results)==J:
           exit(0)            
           return 'Case #1:\n%s'%('\n'.join(results_str))
           
   
if __name__ == '__main__':

    do_debug = True
    input_file = sys.argv[1]
    output_file =  input_file.split('.')[0]+'.out'    
    
    try:
      with open(input_file,'r') as f:
          T = read_int(f) # Number of test cases
          for t in range(1, T+1):
              sys.stdout.write(naive_solver(**main_reader(t,f)))
    except IOError:
       print 'File %s not found'%input_file
       exit(1)       

