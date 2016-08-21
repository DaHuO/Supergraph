#Input      Output
#0          Case #1: INSOMNIA
#1          Case #2: 10
#2          Case #3: 90
#11         Case #4: 110
#1692       Case #5: 5076

def count(case,n):
    digitsSeen=[0,0,0,0,0,0,0,0,0,0]
    i=1
    isInsomnia=False
    lastNumberInHead=0
    numberInHead=n

    while True:
        numberInHead=str(i*n)
        #print "numberInHead = "+str(numberInHead)
        if numberInHead==lastNumberInHead:
            isInsomnia=True
            break
        for digit in numberInHead: 
            digitsSeen[int(digit)]=1
        if sum(digitsSeen)==10:
            break
        lastNumberInHead=numberInHead
        i+=1

    if isInsomnia:
        return "Case #"+str(case)+": INSOMNIA"+"\n"
    else:
        return "Case #"+str(case)+": "+str(numberInHead)+"\n"

def readTestFile(fileName):
    r = open('sheep.out', 'w')
    with open(fileName) as f:
        i=0
        for line in f:
            if i==0:
                NumberOfRecords=int(line)
            else:
                r.write(count(i,int(line.strip('\n'))))
            i+=1  
    r.close()

readTestFile('sheep.in')




    

