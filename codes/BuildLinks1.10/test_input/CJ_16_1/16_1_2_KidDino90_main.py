import re
from collections import Counter
inputFile = open ('input.in', 'r')


def main ():
    listLine = inputFile.read ().splitlines ()
    stage1 (listLine)

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
def stage1 (listLine):
    ###############################################################
    ############                                   ################
    ############        Global Variables           ################
    ############                                   ################
    ###############################################################
    output = []
    global CasePointer
    CasePointer = 1
    for i in range (1, int(listLine[0]) + 1):
        answer = ""
        
        ###############################################################
        ###############################################################
        ###############             START            ##################
        ###############################################################
        ###############################################################
        N = listLine[CasePointer]
        lengthP = 0
        
        for j in range (CasePointer+1, len(listLine)):
            if len(listLine[j].split()) == 1:
               # print("-" + str(j))
               # print("+" + str(CasePointer))
                lengthP = (j) - (CasePointer) - 1
                break
               # print("=" + str(lengthP))
        if lengthP == 0:
            lengthP = len(listLine) - CasePointer - 1
        div = (lengthP+1)/int(N)
        tempList = []
        tempList2 = []
        tempList3 = []
        for j in range (CasePointer + 1, CasePointer+1 +lengthP):
            tempList.extend(listLine[j].split())
        tempList = list(map(int, tempList))
        tempList.sort()
        print(tempList)
        for j in range (0, len(tempList)):
            if tempList[j] not in tempList2:
                tempList2.append(tempList[j])
                tempList3.append(1)
            else:
                index = tempList2.index(tempList[j])
                tempList3[index] = tempList3[index] + 1
        tempList2 = list(map(int, tempList2))
        tempList3 = list(map(int, tempList3))
        for j in range (0, len(tempList3)):
            if int(tempList3[j])% div != 0:
                answer = answer + str(tempList2[j]) + " "
        if(answer[len(answer)-1] == ' '):
            answer = answer[:-1]
        CasePointer = CasePointer + lengthP + 1

        
        

        
        ###############################################################
        ###############################################################
        ###############################################################
        ###############################################################
        ###############################################################
    
        outputLine = "Case #" + str(i) + ": " + answer
        print (outputLine)
        output.append (outputLine)
        printOutput (output)




###############################################################                   
###############################################################
###############################################################
###############################################################
###############################################################
        
def printOutput (output):
    outputFile = open('output', 'w')
    for i in range (0, len (output) - 1):
        outputFile.write (output[i] + "\n")
    outputFile.write (output[len (output) - 1])
            


main()
