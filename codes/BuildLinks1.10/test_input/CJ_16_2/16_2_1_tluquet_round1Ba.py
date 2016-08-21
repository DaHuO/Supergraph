# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:57:22 2016

pbA : theLastWord 

@author: tluquet
"""

import sys 

OUTPUT_FILE = "outPbA.txt"
DIGIT_LIST = ["ZERO", "TWO", "SIX", "EIGHT", "SEVEN", "FIVE","THREE",  "FOUR", "NINE", "ONE"]
DIGIT_EQ = [0,2,6,8,7,5,3,4,9,1]
def main():
    if (len(sys.argv) != 2):
        print "No input file was given"        
        return 0     
    f = open(sys.argv[1],'r')
    
    # I/O Lists  init
    inList = []
    outList = []
    
    #Read from input 
    nbLines = int(f.readline())
    print "There are " + str(nbLines) + " cases:"
    
    for l in xrange(nbLines):
        line = f.readline()
        if(line[-1] == '\n'):
            line = line[:-1]
        inList.append(line)
    print inList
    
    #foreach string S 
    for S in inList: 
        Stemp = S        
        tel = []        
        #For each digit in DigitList
        for j,digitStr in enumerate(DIGIT_LIST):
            found = True
            #Handle multiple times the same number
            while (found):
                if(len(Stemp)>0):            
                    included = True
                    i = 0 
                    while (included and i<len(digitStr)):
                        included = False
                        letter = digitStr[i]
                        if letter in Stemp:
                            included = True
                            i+=1
                    if(i==len(digitStr)):
                        print digitStr + " was found in : " +Stemp
                        #Digit in S
                        tel.append(DIGIT_EQ[j])
                        for letter in digitStr:
                            #Remove the letter for Stemp
                            a = Stemp.split(letter,1)
                            if(len(a) >1):
                                Stemp = a[0]+a[1]
                            else:
                                Stemp = a[0]
                        print Stemp
                    else: 
                        found = False 
                else: 
                    found = False
        if(len(Stemp)>0): 
            print "Error, S was not recovered correctly"
        print tel  
        outList.append(sorted(tel))           
    
    outFile = open(OUTPUT_FILE,'w+')
    i = 1
    for res in outList:
        print "Case #" + str(i) + ": " 
        outFile.write("Case #" + str(i)+ ": ")
        for dig in res : 
            print dig
            outFile.write(str(dig))
        outFile.write("\n")
        i+=1 
    
if __name__ == "__main__":
    main()