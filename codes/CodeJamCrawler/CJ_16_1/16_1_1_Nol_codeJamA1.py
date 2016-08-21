#!/usr/bin/env python3

def lastWord(S):
    lastWord=S[0]
    for c in S[1::]:
        if c>=lastWord[0]:
            lastWord=c+lastWord
        else:
            lastWord=lastWord+c
    return lastWord


def main():
    inFile=open("dataset.txt",'r')
    outFile=open("output.txt",'w')
    caseNumber=int(inFile.readline())
    print("number of case :" + str(caseNumber))
    i=1
    for line in inFile:
        outFile.write("Case #"+str(i)+": "+lastWord(line));
        i=i+1
    inFile.close()
    outFile.close()
    pass


main()