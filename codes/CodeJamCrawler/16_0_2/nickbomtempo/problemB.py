import pandas as pd

def reversePlus(plus):
    if plus == "+":
        return "-"
    return "+"
inputCsv = pd.read_csv("input.txt", header=0)
nInputs = inputCsv.columns.values[0]
answers = []
b = 1
for x in (inputCsv[nInputs].tolist()):
    i = 0
    x = x[::-1]
    notResult = True
    while notResult:
        novo = ""
        needToReverse = False
        for j in range(0, len(x)):
            # print(x)
            if x[j] == '-':
                needToReverse = True
                notResult = True
            else:
                if j == len(x)-1 and not needToReverse:
                    notResult = False
            if needToReverse:
                novo = novo + reversePlus(x[j])
            else:
                novo = novo + x[j]
        if needToReverse:
            i = i + 1
        x = novo
    answers.append(str(b)+": "+str(i))
    b = b + 1
    # print(answers)

f = open('submission.txt','w')
for i in range(0, len(answers)):
    f.write("Case #"+str(answers[i])+'\n')
f.close() # you can omit in most cases as the destructor will call it
