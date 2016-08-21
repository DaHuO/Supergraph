'''
Created on 09-Apr-2016

@author: varunm
'''

global recursionCounter 
recursionCounter = 10000

def checkArray(N,digitDict):        
    for letter in str(N):
        digitDict[letter] = 'True'
        #print digitDict
        if((digitDict['0'] == 'True') and (digitDict['1'] == 'True') and (digitDict['2'] == 'True') and (digitDict['3'] == 'True') and (digitDict['4'] == 'True') and (digitDict['5'] == 'True') and (digitDict['6'] == 'True') and (digitDict['7'] == 'True') and (digitDict['8'] == 'True') and (digitDict['9'] == 'True')):
            return True
            
    
def CountSheep(caseNo, inputNumber):
    digitDict = {'0': 'False','1': 'False','2': 'False','3': 'False','4': 'False','5': 'False','6': 'False','7': 'False','8': 'False','9': 'False'};
    insomnia = True
    for i in range(1,recursionCounter+1):
        N = int(inputNumber)*i
        #print "checking for N : ",N
        if(checkArray(N, digitDict)):
            print "Case #"+str(caseNo)+":",N
            insomnia = False
            break
    if(insomnia):
        print "Case #"+str(caseNo)+": INSOMNIA"     

def fileRead():
    fo = open("input.txt", "rw+")
    lineList = fo.readlines()
    noTestCases = int(lineList[0])  
    for i in range(1, noTestCases+1):
        #print "Case #",i," : ",lineList[i]        
        CountSheep(i,lineList[i])

def main():
    fileRead()
    
if __name__ == "__main__":
    main()