# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 21:27:32 2016

@author: jon
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 00:30:30 2016

@author: jon
"""
# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io
import string
import heapq

d = dict(enumerate(string.ascii_uppercase,0))

def move(Li):
    if sum(Li)!=3:
        poses=heapq.nlargest(2, xrange(len(Li)), key=Li.__getitem__)
        newLi=Li
        po=poses[0] 
        newLi[po]=newLi[po]-1
        poo=poses[1]
        newLi[poo]=newLi[poo]-1
        dd=[d[po],d[poo]]
        ddd="".join(dd)
    else:
        poses=heapq.nlargest(1, xrange(len(Li)), key=Li.__getitem__)
        newLi=Li
        po=poses[0] 
        newLi[po]=newLi[po]-1
        dd=[d[po]]
        ddd="".join(dd)
    return([newLi,[ddd]])
  
def solveA(Li):
    moves=list()
    while sum(Li)>0:
        B=move(Li)
        Li=B[0]
        moves=moves+B[1]
    mover=" ".join(moves)
    return(mover)
    
def solve(infname, outfname):
    L= codejam_io.read_simple_2(infname, int)
    results = [solveA(Li) for Li in L]
    codejam_io.write_simple(outfname,results)
   
    
#solve("A-sample.in", "A-sample.out")   
#solve("A-small-attempt0.in", "A-small-attempt0.out")    
#solve("A-small-attempt1.in", "A-small-attempt1.out")   
#solve("A-small-attempt2.in", "A-small-attempt2.out")     
solve("A-large.in", "A-large.out")     