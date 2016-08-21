# -*- coding: utf-8 -*-
"""
 
@author: Luca
"""

# General imports
#import numpy as np
#import scipy as sc
import itertools
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
    S= read_word(f)
    return {'T':T,'S':S}    


    

def enumeration_solver(T,S=None):
   """
   
   """
   #digits = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
   #values= range(0,10)
   num = []
   while len(S)>0:
     if S.find('Z')!=-1:
       num.append(0)
       # Now remove 'E','R','O'
       S = S.replace('Z','',1)
       S = S.replace('E','',1)
       S = S.replace('R','',1)
       S = S.replace('O','',1)
       continue

     if S.find('X')!=-1:
       num.append(6)
       # Now remove 'I,'X'
       S = S.replace('S','',1)
       S = S.replace('I','',1)
       S = S.replace('X','',1)
       continue
       
     if S.find('W')!=-1:
       num.append(2)
       # Now remove 'T','O'
       S = S.replace('T','',1)
       S = S.replace('W','',1)
       S = S.replace('O','',1)
       continue

     if S.find('U')!=-1:
       num.append(4)
       # Now remove 'T','O'
       S = S.replace('F','',1)
       S = S.replace('O','',1)
       S = S.replace('U','',1)
       S = S.replace('R','',1)
       continue

     if S.find('F')!=-1:
       num.append(5)
       # Now remove 'T','O'
       S = S.replace('F','',1)
       S = S.replace('I','',1)
       S = S.replace('V','',1)
       S = S.replace('E','',1)
       continue

     if S.find('V')!=-1:
       num.append(7)
       # Now remove 'T','O'
       S = S.replace('S','',1)
       S = S.replace('E','',1)
       S = S.replace('V','',1)
       S = S.replace('E','',1)
       S = S.replace('N','',1)
       continue
 
     if S.find('O')!=-1:
       num.append(1)
       # Now remove 'T','O'
       S = S.replace('O','',1)
       S = S.replace('N','',1)
       S = S.replace('E','',1)
       continue

     if S.find('N')!=-1:
       num.append(9)
       # Now remove 'T','O'
       S = S.replace('N','',1)
       S = S.replace('I','',1)
       S = S.replace('N','',1)
       S = S.replace('E','',1)
       continue

     if S.find('G')!=-1:
       num.append(8)
       # Now remove 'T','O'
       S = S.replace('E','',1)
       S = S.replace('I','',1)
       S = S.replace('G','',1)
       S = S.replace('H','',1)
       S = S.replace('T','',1)
       continue

     if S.find('H')!=-1:
       num.append(3)
       # Now remove 'T','O'
       S = S.replace('T','',1)
       S = S.replace('H','',1)
       S = S.replace('R','',1)
       S = S.replace('E','',1)
       S = S.replace('E','',1)
       continue

   num.sort()
   return 'Case #%d: %s\n'%(T,''.join([str(t) for t in num]))
   
if __name__ == '__main__':

    do_debug = True
    input_file = sys.argv[1]
    output_file =  input_file.split('.')[0]+'.out'    
    
    try:
      with open(input_file,'r') as f:
          T = read_int(f) # Number of test cases
          for t in range(1, T+1):
              sys.stdout.write(enumeration_solver(**main_reader(t,f)))
    except IOError:
       print 'File %s not found'%input_file
       exit(1)       

