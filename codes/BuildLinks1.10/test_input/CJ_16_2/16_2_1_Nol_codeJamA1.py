#!/usr/bin/env python3

def phoneNumber(S):
    modifiedS=S
    number=[]
    while 'Z' in modifiedS:
        number.append(0)
        modifiedS=modifiedS.replace("Z","",1)
        modifiedS=modifiedS.replace("E","",1)
        modifiedS=modifiedS.replace("R","",1)
        modifiedS=modifiedS.replace("O","",1)
    while 'X' in modifiedS:
        number.append(6)
        modifiedS=modifiedS.replace("S","",1)
        modifiedS=modifiedS.replace("I","",1)
        modifiedS=modifiedS.replace("X","",1)
    while 'W' in modifiedS:
        number.append(2)
        modifiedS=modifiedS.replace("T","",1)
        modifiedS=modifiedS.replace("W","",1)
        modifiedS=modifiedS.replace("O","",1)
    while 'S' in modifiedS:
        number.append(7)
        modifiedS=modifiedS.replace("S","",1)
        modifiedS=modifiedS.replace("E","",1)
        modifiedS=modifiedS.replace("V","",1)
        modifiedS=modifiedS.replace("E","",1)
        modifiedS=modifiedS.replace("N","",1)
    while 'V' in modifiedS:
        number.append(5)
        modifiedS=modifiedS.replace("F","",1)
        modifiedS=modifiedS.replace("I","",1)
        modifiedS=modifiedS.replace("V","",1)
        modifiedS=modifiedS.replace("E","",1)
    while 'F' in modifiedS:
        number.append(4)
        modifiedS=modifiedS.replace("F","",1)
        modifiedS=modifiedS.replace("O","",1)
        modifiedS=modifiedS.replace("U","",1)
        modifiedS=modifiedS.replace("R","",1)
    while 'G' in modifiedS:
        number.append(8)
        modifiedS=modifiedS.replace("E","",1)
        modifiedS=modifiedS.replace("I","",1)
        modifiedS=modifiedS.replace("G","",1)
        modifiedS=modifiedS.replace("H","",1)
        modifiedS=modifiedS.replace("T","",1)
    while 'T' in modifiedS:
        number.append(3)
        modifiedS=modifiedS.replace("T","",1)
        modifiedS=modifiedS.replace("H","",1)
        modifiedS=modifiedS.replace("R","",1)
        modifiedS=modifiedS.replace("E","",1)
        modifiedS=modifiedS.replace("E","",1)
    while 'I' in modifiedS:
        number.append(9)
        modifiedS=modifiedS.replace("N","",1)
        modifiedS=modifiedS.replace("I","",1)
        modifiedS=modifiedS.replace("N","",1)
        modifiedS=modifiedS.replace("E","",1)
    while 'O' in modifiedS:
        number.append(1)
        modifiedS=modifiedS.replace("O","",1)
        modifiedS=modifiedS.replace("N","",1)
        modifiedS=modifiedS.replace("E","",1)
    #sort numbers list
    number.sort()
    print(number)
    sPhone=""
    for i in number:
        sPhone+=str(i)
    print(sPhone)
    return sPhone
    pass



def main():
    inFile=open("dataset.txt",'r')
    outFile=open("output.txt",'w')
    caseNumber=int(inFile.readline())
    print("number of case :" + str(caseNumber))
    i=1
    for line in inFile:
        outFile.write("Case #"+str(i)+": "+phoneNumber(line)+"\n");
        i=i+1
    inFile.close()
    outFile.close()
    pass



main()