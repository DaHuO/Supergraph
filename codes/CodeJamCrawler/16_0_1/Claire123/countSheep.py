#!/usr/bin/env python

inFile="A-large.in"
cases=[]
with open(inFile) as f:
    content=f.readlines()
    caseNum=int(content[0].strip('\n'))
    for en in range(caseNum):
        oneCase=content[en+1].strip('\n')
        cases.append(oneCase)
f.close()


for en in range(len(cases)):
    strNum=''
    for t in range(1,101):
        strNum+=str(t*int(cases[en]))
        record=t*int(cases[en])
        if len(set(strNum))==10:
            break
    if record==0:
        print "Case #"+str(en+1)+": "+"INSOMNIA"
    else:
        print "Case #"+str(en+1)+": "+str(record)