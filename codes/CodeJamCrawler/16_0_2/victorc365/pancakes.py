#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pancakes.py
#  
#  Copyright 2016 Victor  <victor@victor-Lenovo-G40-80>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def main():
    case = 0
    S = raw_input()
    try:
        while(case<=100):
            S=raw_input()
            case = case + 1
            moves = 0
            while(True):
                S = list(S)
                if isHappyString(S):
                    print "Case #{}: {}".format(case,moves)
                    break
                else:
                    while not isHappyString(S):
                        partition = cambio_de_signo(S)
                        if(partition!=-1):
                            moves = moves + 1
                            S=refleja(S,partition-1)
                        else:
                            moves = moves + 1
                            j = len(S)-1        
                            S = refleja(S,j)
                    print "Case #{}: {}".format(case,moves)
                    break
        
        
    except (EOFError):
        return 0    
    return 0
    
def isHappyString(S):
    for i in range(len(S)):
        if S[i]!='+':
            return False
    return True 
    
    
def refleja(L,j):
    # reflect the first j elements of L an return the relfect and the inverse orden
    R = []
    for i in range(j+1):
        if L.pop(0) == '+':
            R.append('-')
        else:
            R.append('+')
    if len(L)!=0:
        R.extend(L)
    return R

def cambio_de_signo(L):
    for i in range(len(L)):
        if L[0]!=L[i]:
            return i
    return -1
        
        
        
        
if __name__ == '__main__':
    main()

