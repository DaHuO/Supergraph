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


def solveA(Str):
    st=Str[0]
    st=''.join(sorted(st))
    count=[0]*10
    count[0]=st.count("Z")
    count[2]=st.count("W")
    count[4]=st.count("U")
    count[6]=st.count("X")
    count[8]=st.count("G")
    count[1]=st.count("O")-count[0]-count[2]-count[4]
    count[3]=st.count("H")-count[8]
    count[5]=st.count("F")-count[4]
    count[7]=st.count("S")-count[6]
    count[9]=st.count("I")-count[5]-count[6]-count[8]
    B=[0]*count[0]+[1]*count[1]+[2]*count[2]+[3]*count[3]+[4]*count[4]+[5]*count[5]+[6]*count[6]+[7]*count[7]+[8]*count[8]+[9]*count[9]
    k=len(B)
    for i in range(0,k):
        B[i]=str(B[i])
    B="".join(B)
    return(B)
    
def solve(infname, outfname):
    L= codejam_io.read_simple(infname, str)
    results = [solveA(Li) for Li in L]
    codejam_io.write_simple(outfname,results)
   
    
#solve("A-sample.in", "A-sample.out")   
#solve("A-small-attempt0.in", "A-small-attempt0.out")    
#solve("A-small-attempt1.in", "A-small-attempt1.out")   
#solve("A-small-attempt2.in", "A-small-attempt2.out")     
solve("A-large.in", "A-large.out")     