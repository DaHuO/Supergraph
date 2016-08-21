# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 07:55:19 2016

@author: BCLAES
"""

def handle_case(N):
    nr = ""
    nrs = []
    N = N.strip()
    while "Z"in N:
        nrs.append(0)
        N = N.replace("Z","",1)        
        N = N.replace("E","",1)
        N = N.replace("R","",1)
        N = N.replace("O","",1)
    while "G" in N:
        nrs.append(8)
        N = N.replace("E","",1)        
        N = N.replace("I","",1)
        N = N.replace("G","",1)
        N = N.replace("H","",1)
        N = N.replace("T","",1)
    while "U" in N:
        nrs.append(4)
        N = N.replace("F","",1)        
        N = N.replace("O","",1)
        N = N.replace("U","",1)
        N = N.replace("R","",1)
        
    while "W" in N:
        nrs.append(2)
        N = N.replace("T","",1)        
        N = N.replace("W","",1)
        N = N.replace("O","",1)
        
    while "X" in N:
        nrs.append(6)
        N = N.replace("S","",1)        
        N = N.replace("I","",1)
        N = N.replace("X","",1)
        
    while "S" in N:             
        nrs.append(7)
        N = N.replace("S","",1)        
        N = N.replace("E","",1)
        N = N.replace("V","",1)
        N = N.replace("E","",1)
        N = N.replace("N","",1)
    
    while "H" in N:
        nrs.append(3)
        N = N.replace("T","",1)        
        N = N.replace("H","",1)
        N = N.replace("R","",1)
        N = N.replace("E","",1)
        N = N.replace("E","",1)
    
    while "V" in N:
        nrs.append(5)
        N = N.replace("F","",1)        
        N = N.replace("I","",1)
        N = N.replace("V","",1)
        N = N.replace("E","",1)
   
    while "I" in N:
        nrs.append(9)
        N = N.replace("N","",1)        
        N = N.replace("I","",1)
        N = N.replace("E","",1)
        N = N.replace("N","",1)
    
    while "N" in N:
        nrs.append(1)
        N = N.replace("O","",1)        
        N = N.replace("N","",1)
        N = N.replace("E","",1)        

  
    #assert len(N) == 0
    print "N = {}".format(N)
    nrs.sort()
    #print nrs
    for i in nrs:
        nr = nr + str(i)
    return nr
    
#print handle_case("OZONETOWER\n")
#print handle_case("WEIGHFOXTOURIST")
#print handle_case("OURNEONFOE")
#print handle_case("ETHER")

	
#
#Case #1: 012
#Case #2: 2468
#Case #3: 114
#Case #4: 3



        
solutions = []
#with open("A-small.in") as f:
with open("A-large.in") as f:
    test_cases = int(f.readline())
    for i in xrange(0,test_cases):
        #DONT FORGET STRIP
        m = f.readline()
        x = handle_case(m)
        strout = str.format("Case #{}: {}\n", i+1, x)
        solutions.append(strout)
with open("output-large.txt", "w") as out:
        out.writelines(solutions)