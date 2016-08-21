# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:57:22 2016

@author: tluquet
"""

import sys 

OUTPUT_FILE = "outPbA.txt"

def main():
    if (len(sys.argv) != 2):
        print "Error while reading argv1"        
        return 0     
    f = open(sys.argv[1],'r')
    
    # I/O Lists  init
    inList = []
    outList = []
    
    #Read from input 
    nbLines = int(f.readline())
    print nbLines
    for l in xrange(nbLines):
        line = int(f.readline())
        inList.append(line)
    print inList
    
    #Now find the results and put it in outList
    for N in inList:
        digList = []
        count = N
        it = 1 
        if(N == 0):
            outList.append("INSOMNIA")
        else:
            while len(digList) != 10 :             
                count = it*N
                for digit in str(count) :               
                    if digit not in digList:
                        digList.append(digit)
                it += 1
            outList.append(str(count))  
                
    outFile = open(OUTPUT_FILE,'w+')
    i = 1
    for res in outList:
        print "Case #" + str(i) + ": " + res
        outFile.write("Case #" + str(i)+ ": " + res + '\n')
        i+=1 
    
if __name__ == "__main__":
    main()