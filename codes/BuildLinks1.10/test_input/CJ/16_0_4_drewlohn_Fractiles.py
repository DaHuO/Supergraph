import csv as csv

print 'Starting'

inFile = open('D-small-attempt0.in','rb')
data = csv.reader(inFile,delimiter=' ')
numTests = int(data.next()[0])

outFile = open('outputSubmission.csv','wb')
outer = csv.writer(outFile)

maxIterations = 1000000



maxIterations = 100000
for i in xrange(numTests):
    row = data.next()
    K = row[0]
    C = row[1]
    S = row[2]

    tilesString = ''
    for j in xrange(int(K)):
        tilesString += str(j+1) + ' '
    
    outString = 'Case #' + str(i+1) + ': ' + tilesString
    print outString
    outer.writerow([outString])

inFile.close()
outFile.close()
            
        

print 'Done'
