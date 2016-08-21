'''for i in inputString:
          
Created on 16-Apr-2016

@author: varunm
'''

def CheckWordArray(wordArray):
    pass

def SolveLastWord(caseNo, inputString, wordArray):
    #print "Input String : "+inputString
    firstChar = inputString[0]
    #print "First Char : "+firstChar
    if(len(wordArray) == 0):
        wordArray.append(firstChar)
        inputString = inputString[1:]
    else:
        newList = []
        for j in wordArray:
            #print ">>  "+j
            if(j[:1]>firstChar):            
                word1 = firstChar+j
                word2=j+firstChar
            else:
                word2 = firstChar+j
                word1=j+firstChar
            #print "Word 1 : "+word1
            #print "Word 2 : "+word2
            newList.append(word1)
            newList.append(word2)
        for x in newList:
            wordArray.append(x)
        inputString = inputString[1:]
    #print wordArray 
    if(len(inputString)>0):           
        SolveLastWord(caseNo, inputString, wordArray)
    else:
        xstr = wordArray[-1]
        print "Case #"+str(caseNo)+":",xstr
        
            

def fileRead():
    fo = open("input.txt", "rw+")
    lineList = fo.readlines()
    noTestCases = int(lineList[0])    
    for i in range(1, noTestCases+1):
        wordArray = []
        #print "Case #",i," : ",lineList[i]        
        SolveLastWord(i,lineList[i],wordArray)

def main():
    fileRead()
    
if __name__ == "__main__":
    main()