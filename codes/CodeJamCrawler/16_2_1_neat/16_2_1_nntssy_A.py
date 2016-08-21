def wordInStr(word,strDict):
    copyDict={}
    for letter in strDict.keys():
        copyDict[letter]=strDict[letter]
    for letter in word:
        if letter in copyDict.keys() and copyDict[letter]>0:
            copyDict[letter]-=1
        else:
            return False
    return True
                    
def updateStr(strDict,word):
    copyDict={}
    for letter in strDict.keys():
        copyDict[letter]=strDict[letter] 
    for letter in word:
        if letter in copyDict.keys() and copyDict[letter]>0:
            copyDict[letter]-=1
            if copyDict[letter]==0:
                del copyDict[letter]
    return copyDict          

def strToTellNum(S):
    tell=''
    tellNum=[]
    strDict={}
    for letter in S:
        if letter in strDict.keys():
            strDict[letter]+=1
        else:
            strDict[letter]=1
    numList=['ZERO','TWO','FOUR','SIX','EIGHT','ONE','THREE','FIVE','SEVEN','NINE']        
    numDict={'ZERO':0,'ONE':1,'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9}
    for numWord in numList:
        while wordInStr(numWord,strDict):
            tellNum.append(numDict[numWord])
            strDict=updateStr(strDict,numWord) 
    tellNum.sort()
    for num in tellNum:
        tell+=str(num)            
    return tell
           
def main(fin,fout):
    numCases=int(fin.readline())
    for i in range(numCases):
        case=fin.readline()
        fout.write('Case #'+str(i+1)+': '+strToTellNum(case)+'\n')
        
fin=open('C:\Users\exin1\Google Drive\Study\Google CodeJam 2016\Round 1B\A2.in','r')
fout=open('C:\Users\exin1\Google Drive\Study\Google CodeJam 2016\Round 1B\A2.out','w')
main(fin,fout)
fin.close()
fout.close()            