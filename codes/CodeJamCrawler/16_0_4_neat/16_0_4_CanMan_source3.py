import math

def printCase(valList, i, out):
    values = ''
    for n in valList:
        values = values + str(int(n)) + ' '
    out.write('Case #' + str(i) + ': ' + values.strip() + '\n')
    return

def printCaseImp(i, out):
    out.write('Case #' + str(i) + ': ' 'IMPOSSIBLE' + '\n')
    return

filename = 'D-small-attempt0.in.'
filenameout = 'filthyGradStudents.out'
f = open('C:\Users\Brian\Documents\Pythonscratch\GoogleCodeJam2016\Qualifiers\Problem4\\' + filename, 'r')
first = f.readline()
out = open('C:\Users\Brian\Documents\Pythonscratch\GoogleCodeJam2016\Qualifiers\Problem4\\' + filenameout, 'w')

i = 0
for line in f:
    i += 1
    k, c, s = line.split(" ", 3)
    s = s.strip()
    k = int(k)
    c = int(c)
    s = int(s)
    valList = []
    index = math.floor((k**(c-1)) / 2)
    if s < k:
        printCaseImp( i, out)
        continue
    elif k == 1:
        printCase([1], i , out)
        continue
    elif (index < 1):
        index = 1
    for j in range(0, k):
        valList.append(index + ((k**(c-1))* j))
    printCase(valList, i , out)

    
    
f.close()
out.close()
print 'done'
    
