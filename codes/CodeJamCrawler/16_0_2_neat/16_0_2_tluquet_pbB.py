# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:57:22 2016

- GOOGLE Code Jam Problem B 

@author: tluquet
"""

import sys 

OUTPUT_FILE = "outPbB.txt"

def flip(stack,iMax):
    
    stackTemp = []
    for p in reversed(xrange(iMax+1)):
        stackTemp.append(-stack[p])
    if(len(stack) != iMax):
        return stackTemp+stack[iMax+1:]    
    else:
        return stackTemp
        
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
        line = f.readline()
        if(line[-1] == '\n'):
            line = line[:-1]
        inList.append(line)
    print inList
    
    #Do treatement here 
    for pancakes in inList:
        stack = []
        for p in pancakes:
            if(p == '-'):
                stack.append(-1)
            elif(p == '+'):
                stack.append(1)
        nbOp = 0 
        print stack
        while not all(p>0 for p in stack): # test if all the pancakes are on the good side
            iEnd = len(stack)-1
            while(stack[iEnd] > 0 ):
                iEnd -= 1
            # We need to flip the stack at iEnd
                #But make sur the first pancake is a - 
            iFirst = -1
            while(stack[iFirst+1] > 0 ):
                iFirst +=1 
            if(iFirst >= 0 ): # At least the First element is a + 
                stack = flip(stack,iFirst)
                nbOp += 1 
                print stack 
            #Flip the stack at iEnd
            stack = flip(stack,iEnd)
            nbOp +=1
            print stack
        print "------------ Solved ---------------"
        outList.append(str(nbOp))    
                
    outFile = open(OUTPUT_FILE,'w+')
    i = 1
    for res in outList:
        print "Case #" + str(i) + ": " + res
        outFile.write("Case #" + str(i)+ ": " + res + '\n')
        i+=1 
    
if __name__ == "__main__":
    main()