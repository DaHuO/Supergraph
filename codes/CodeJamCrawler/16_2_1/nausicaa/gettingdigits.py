# -*- coding: utf-8 -*-
"""

@author: Robo
"""

import os
import numpy as np
import pandas as pd

folder = "D:/CODE/googlecodejam/gettingdigits"
infile = "A-large.in"
outfile = "A-large.out"


def read_gcj_input():
    cases = []
    with open(os.path.join(folder,infile), 'r') as f:
        for each in xrange(int(f.readline())):
            Araw = f.readline().strip()
            cases.append(Araw)
    return cases

spelled = {0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",
           6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}  
      
cases = read_gcj_input()

with open(os.path.join(folder,outfile), 'w') as f:
    for caseNum,case in enumerate(cases):
        letters = case
        numbers = []
        letterslist = [char for char in letters]
        #can uniquely id zero, two, four, six, eight
        if "Z" in letterslist:
            while "Z" in letterslist:
                letterslist.remove("Z")
                letterslist.remove("E")
                letterslist.remove("R")
                letterslist.remove("O")
                numbers.append(0)
        if "W" in letterslist:
            while "W" in letterslist:
                letterslist.remove("T")
                letterslist.remove("W")
                letterslist.remove("O")
                numbers.append(2)
        if "U" in letterslist:
            while "U" in letterslist:
                letterslist.remove("F")
                letterslist.remove("O")
                letterslist.remove("U")
                letterslist.remove("R")
                numbers.append(4)
        if "X" in letterslist:
            while "X" in letterslist:
                letterslist.remove("S")
                letterslist.remove("I")
                letterslist.remove("X")
                numbers.append(6)
        if "G" in letterslist:
            while "G" in letterslist:
                letterslist.remove("E")
                letterslist.remove("I")
                letterslist.remove("G")
                letterslist.remove("H")
                letterslist.remove("T")
                numbers.append(8)
        #one, three, five, seven, nine still remaining
        if "V" in letterslist:
            while "V" in letterslist:
                if "F" in letterslist:
                    letterslist.remove("F")
                    letterslist.remove("I")
                    letterslist.remove("V")
                    letterslist.remove("E")
                    numbers.append(5)
                else:
                    letterslist.remove("S")
                    letterslist.remove("E")
                    letterslist.remove("V")
                    letterslist.remove("E")
                    letterslist.remove("N")
                    numbers.append(7)
        if "R" in letterslist:
            while "R" in letterslist:
                letterslist.remove("T")
                letterslist.remove("H")
                letterslist.remove("R")
                letterslist.remove("E")
                letterslist.remove("E")
                numbers.append(3)
        if "I" in letterslist:
            while "I" in letterslist:
                letterslist.remove("N")
                letterslist.remove("I")
                letterslist.remove("N")
                letterslist.remove("E")
                numbers.append(9)
        if "N" in letterslist:
            while "N" in letterslist:
                letterslist.remove("O")
                letterslist.remove("N")
                letterslist.remove("E")
                numbers.append(1)
            
        numbers.sort()
        numasstring = [str(num) for num in numbers]
                
        f.write('Case #{0}: {1}\n'.format(caseNum+1,''.join(numasstring)))
