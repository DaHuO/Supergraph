# -*- coding: utf-8 -*-
"""
 
@author: Luca
"""

# General imports
#import numpy as np
#import scipy as sc
#import pandas as pd
#import itertools
import re
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
    
    # Here need to read each individual test case.
    #D = read_int(f)
    data=read_word(f)
    #data = np.array(read_arr(f,1,reader=read_letters))


    return {'T':T,'seqe':[data]}    
    
def greedy_solver(T,D=None,data=None):
    # At each time we can either:
    # a) let people eat pancakes in this case the data array would be decremented by 1
    # b) choose one person and take a given number of pancakes and give them to another person.
    #    In this case the optimal choice will be to take the pancakes from the person having the
    #    most and giving to a person having none. The number of pancakes to distrubute
    #    should be optimized taking into account multiple subdivisions.
    #    It makes sense to subdivide the larges stash in (almost) equal parts
    #    the more (smaller) parts I create the more times we need to wait
    #    when the bound on the remaining times is greater than the bound on 
    #    the second max value then we need to stop
   
    #   in this case the optimal solution would be to take half of thepancakes from the person 
    #   with the  highest number of pancakes and give them to a person with no pancakes at all
    #   under a) the expected number of remaining times is bound by the max number 
    #   of pancakes a person has Dmax
    #   Redistributing the remaing times will be bound by the maximum between ceil(Dmax/2)+1
    #   and the highest value > Dmax/2
    data = np.sort(data)
    data = np.insert(data,[0],[0])# Insert dummy person with no pancakes
    cnt = 0
    Dmax = data[-1]
    while Dmax>0:
       # Evaluate optima subdivision on Dmax if any
       # initial guess for half 
       tmp = np.ceil(Dmax*0.5)
       bound1 = max([tmp+1,data[-2]])
       
       #for nn in range(3,Dmax):
       # Evaluate bound on remaining moves 
       bound1 = max([tmp+1,data[-2]])
       bound2 = Dmax # No distribution
       if (bound1<bound2):
          data[-1]= data[-1]-tmp
          data = np.insert(data,[0],[tmp])
          data = np.sort(data)           
       else:
          data[1:] = data[1:]-1  
       
       cnt +=1
       Dmax = data[-1]  

    return 'Case #%s: %d\n' % (T, cnt)    

def optimal_subdivision(Dmax,D2max):
# Given a maximum number of pancakes and the calculates the
# best scoring subdivision in equal parts
# - the number of subdivision to be test range between 2 and
# - the 2nd maximum number of pancakes, any subdivision in higher
#   number of subset leads to suboptimal solution.
    opt = np.max([D2max,np.ceil(float(Dmax)/2)])+1
    nopt = 2
    for n in range(2,Dmax/2+2):
        bound = np.max([np.ceil(float(Dmax)/n),D2max])+(n-1)
        if  (bound<opt):
            nopt = n
            opt = bound
        #if bound <=D2max:
        #    break

    return nopt,opt


 

class dumb_solver:
    
   def __init__(self):     
     self.search_store = {}
     self.solution = []
  
   def doflip(self,data,index):
      if (index == 0):
        if data[0]=='-':
          return( '+%s'%(data[1:]))
        else:
          return( '-%s'%(data[1:]))
      else:      
        return( '%s%s'%(data[index::-1].replace('+','*').replace('-','+').replace('*','-'),data[index+1:]))
   
   def solve(self,T,seqe=[],res=[],level=0,regex=re.compile(r"-*")):
      #print 'At level %d %s soluzione:%d'%(level,','.join(seqe),len(self.solution))    
      if level>1*len(seqe[-1]):
          return
      if not re.search(r'-+',seqe[-1]):
         #print 'Trovata soluzione %s'%(seqe[-1])
         if (len(self.solution)>len(seqe) or len(self.solution)==0):
              self.solution = seqe
         return
        
      self.search_store[seqe[-1]]= level 
    
      for idx in range(0,len(seqe[-1])):
          
        flipped = self.doflip(seqe[-1],idx)
        #print 'original %s idx %d flipped %s'%(seqe[-1],idx,flipped)
        if  self.search_store.has_key(flipped):
            if self.search_store[flipped]<=level:
               #print 'stopped on sequence %s'%flipped
              continue            
        self.solve(T,seqe + [flipped],res,level+1,regex)
  
      return 
      return 'Case #%s: %d\n' % (T, cnt_min)    
       
    
if __name__ == '__main__':

    do_debug = True
    input_file = sys.argv[1]
    output_file =  input_file.split('.')[0]+'.out'    
    
    try:
      with open(input_file,'r') as f:
          T = read_int(f)
          for t in range(1, T+1):
              solver = dumb_solver()
              
              solver.solve(**main_reader(t,f))
              sys.stdout.write('Case #%s: %d\n'%(t, len(solver.solution)-1))
    except IOError:
       print 'File %s not found'%input_file
       exit(1)       

