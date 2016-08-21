import math as ma
import pandas as pd
import collections

inputCsv = pd.read_csv("input.txt", header=1)
nInputs = inputCsv.columns.values[0]
listRange = set()
for l in range(0,10):
    listRange.add(l)
t = 1
answers = []
count = 0
for x in (inputCsv[nInputs].tolist()):
    count = count+1
    aux = x
    listDigits = set()
    resultado = True
    t = 0
    while(resultado and t<=200):
        t=t+1
        x = int(aux) * t
        x = str(x)

        for digit in x:
            listDigits.add(int(digit))
        exist = True
        for i in listRange:
            if i in listDigits:
                exist = True and exist
            else:
                exist = False
        resultado=not exist

    if resultado == False:
        answers.append(str("Case #"+str(count)+": "+str(x)))
    else:
        answers.append(str("Case #"+str(count)+": INSOMNIA"))
f = open('submission.txt','w')
for i in range(0, len(answers)):
    f.write(answers[i]+'\n')
f.close() # you can omit in most cases as the destructor will call it
