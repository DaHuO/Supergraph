import csv as csv

print 'Starting'

#inFile = open('A-large-practice.in','rb')
inFile = open('A-large.in','rb')
data = csv.reader(inFile,delimiter=' ')
numTests = int(data.next()[0])

outFile = open('testOutput01.csv','wb')
outer = csv.writer(outFile)

def digitFinder(digit, number):
    numString = str(number)
    if digit in numString:
        return True
    else:
        return False


maxIteration = 1000000

for i in xrange(numTests):
    N = int(data.next()[0])
    if N == 0:
        outString = 'Case #' + str(i+1) + ': ' + 'INSOMNIA'
        outer.writerow([outString])
        continue

    numbersList = ['0','1','2','3','4','5','6','7','8','9']
    for j in xrange(maxIteration):        
        foundList = []
        j += 1
        for number in numbersList:
            if digitFinder(number,j*N):
                foundList.append(number)
        for number in foundList:
            if number in foundList:
                numbersList.remove(number)
        if numbersList == []:
            break
        if j==(maxIteration-1):
            print 'Warning: max iteration hit'
            outString = 'Case #' + str(i+1) + ': ' + 'INSOMNIA'
            outer.writerow([outString])
            continue
        
    outString = 'Case #' + str(i+1) + ': ' + str(j*N)
    outer.writerow([outString])

inFile.close()
outFile.close()
            
        

print 'Done'
