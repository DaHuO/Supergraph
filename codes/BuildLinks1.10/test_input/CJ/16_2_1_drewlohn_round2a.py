import csv as csv

print 'Starting'

inFile = open('A-small-attempt1.in','rb')
data = csv.reader(inFile,delimiter=' ')
numTests = int(data.next()[0])

outFile = open('outputSubmission.csv','wb')
outer = csv.writer(outFile)
##outString = 'Case #1:' 
##outer.writerow([outString])


letters = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

def removeNumber(string, num):
    sList = list(string)
    for letter in letters[num]:
        loc = sList.index(letter)        
        sList.pop(loc)    
    return str(sList)



count = 0
for i in xrange(numTests):
    s = data.next()[0]
    print s
    phoneNum = []
    while 'Z' in s:
        phoneNum.append(0)
        s = removeNumber(s,0)
    while 'W' in s:
        phoneNum.append(2)
        s = removeNumber(s,2)
    while 'U' in s:
        phoneNum.append(4)
        s = removeNumber(s,4)
    while 'X' in s:
        phoneNum.append(6)
        s = removeNumber(s,6)
    while 'G' in s:
        phoneNum.append(8)
        s = removeNumber(s,8)
    while 'H' in s:
        phoneNum.append(3)
        s = removeNumber(s,3)
    while 'F' in s:
        phoneNum.append(5)
        s = removeNumber(s,5)
    while 'I' in s:
        phoneNum.append(9)
        s = removeNumber(s,9)
    while 'V' in s:
        phoneNum.append(7)
        s = removeNumber(s,7)
    while 'N' in s:
        phoneNum.append(1)
        s = removeNumber(s,1)


    phoneNum.sort()
    answer = ''
    for val in phoneNum:
        answer += str(val)

    outString = 'Case #' + str(i+1) + ': ' + answer
    #print outString
    outer.writerow([outString])

inFile.close()
outFile.close()
            
        

print 'Done'
