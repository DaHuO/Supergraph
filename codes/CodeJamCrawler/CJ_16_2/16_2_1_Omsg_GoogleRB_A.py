'''
Created on 30. Apr. 2016

@author: oli
'''
import numpy as np

# ---- config ---- #

FileInput="C:\data\dataRB_A.in"
FileOutput="C:\data\dataRB_A_new.out"

# ---------------- #

def start(s):
    resultNumber=np.array([0]*10)
    word=list(s)
    num=checkNumberOfChar("Z",word)
    print word
    if num>0:
        word=deleteNumberFromChar(0,word,num)
        resultNumber[0]=num
        
    print "8"
    print word
    num=checkNumberOfChar("G",word)
    if num>0:
        word=deleteNumberFromChar(8,word,num)
        resultNumber[8]=num
        
    print "6"
    print word
    num=checkNumberOfChar("X",word)
    if num>0:
        word=deleteNumberFromChar(6,word,num)
        resultNumber[6]=num
            
    print "7"
    print word
    num=checkNumberOfChar("S",word)
    if num>0:
        word=deleteNumberFromChar(7,word,num)
        resultNumber[7]=num
        
    print "2"
    print word
    num=checkNumberOfChar("W",word)
    if num>0:
        word=deleteNumberFromChar(2,word,num)
        resultNumber[2]=num
        
    print "5"
    print word
    num=checkNumberOfChar("V",word)
    if num>0:
        word=deleteNumberFromChar(5,word,num)
        resultNumber[5]=num
        
    print "4"
    print word
    num=checkNumberOfChar("U",word)
    if num>0:
        word=deleteNumberFromChar(4,word,num)
        resultNumber[4]=num
        
    print "9"
    print word
    num=checkNumberOfChar("I",word)
    if num>0:
        word=deleteNumberFromChar(9,word,num)
        resultNumber[9]=num
        
    print "3"
    print word
    num=checkNumberOfChar("H",word)
    if num>0:
        word=deleteNumberFromChar(3,word,num)
        resultNumber[3]=num
        
    print "1"
    print word
    num=checkNumberOfChar("O",word)
    if num>0:
        word=deleteNumberFromChar(1,word,num)
        resultNumber[1]=num
    
    print word
    result=""
    for i in range(10):
        for j in range(resultNumber[i]):
            result=result+str(i)
    return result     
             
def file_load():
    check=[]
    with open(FileInput) as f:
        for line in f:
            check.append(str(line).replace("\n",""))
    return check

def checkNumberOfChar(char, string):
    number=0
    for x in string:
        if x==char:
            number=number+1           
    return number

def deleteNumberFromChar(number,word,amount):
    while amount>0:
        numberLetters=getNumber(number)
        numberL=list(numberLetters)
        j=0
        for x in word:
            i=0
            for l in numberL:
                if x==l:
                    numberL[i]=""
                    word[j]=""
                i=i+1
            j=j+1
        amount=amount-1
    return word
    
def getNumber(i):
    if i==0:
        return "ZERO"
    elif i==1:
        return "ONE"
    elif i==2:
        return "TWO"
    elif i==3:
        return "THREE"
    elif i==4:
        return "FOUR"
    elif i==5:
        return "FIVE"
    elif i==6:
        return "SIX"
    elif i==7:
        return "SEVEN"
    elif i==8:
        return "EIGHT"
    elif i==9:
        return "NINE"

def normal_mode():
    result = start("FINVEVSENEINESXI")
    print "------------------------------------"
    print "Result: "+result
    print "------------------------------------"
        
def array_mode():
    f = open(FileOutput, 'w')
    check = file_load()
    print check
    for i in range(np.size(check)):
        if i>0:
            line=check[i].split(" ")
            K=line[0]
            writeString = "Case #"+str(i)+": "+str(start(K))
            f.write(writeString+"\n")
            print writeString
    print "------------------------------------"
                       
if __name__ == "__main__":
    print "------------------------------------"
    print "Start program"
    print "------------------------------------"
    array_mode()
    
    