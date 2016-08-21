import csv as csv

print 'Starting'

inFile = open('B-large (1).in','rb')
data = csv.reader(inFile,delimiter=' ')
numTests = int(data.next()[0])

outFile = open('outputSubmission.csv','wb')
outer = csv.writer(outFile)

maxIterations = 1000000


def flipper(revPstring, l):
    toStay = revPstring[0:l]
    toFlip = revPstring[l::]
    flipped = ''
    for val in toFlip[::-1]:
        if val == '+':
            flipped += '-'
        if val == '-':
            flipped += '+'
    #print toStay, flipped
    return ''.join(toStay) + flipped

def countBack(revPstring):
    l = len(revPstring)
    for i in xrange(l):
        if revPstring[(l-1)-i]=='-':
            return (l-1)-i + 1

def countUp(revPstring):
    l = len(revPstring)
    for i in xrange(l):
        if revPstring[i] == '-':
            return i

maxIterations = 100000
for i in xrange(numTests):
    pString = data.next()[0]
    revPstring = pString[::-1]

    for flipCount in xrange(maxIterations):
        if '-' not in revPstring:
            break
        elif revPstring[-1] == '+':
            flipIndex = countBack(revPstring)        
        else:
            flipIndex = countUp(revPstring)
        revPstring = flipper(revPstring,flipIndex)
            
        
    if flipCount == maxIterations-1:
        print 'Warning: Max Iterations'
    outString = 'Case #' + str(i+1) + ': ' + str(flipCount)
    outer.writerow([outString])

inFile.close()
outFile.close()
            
        

print 'Done'
