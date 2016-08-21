# Fractile

infile = open("D-small-attempt0.in",'r')
casenum = int(infile.readline())
ofile = open('D-small-attempt0.txt','w')

for i in range(casenum):
    print 'Case #'+str(i+1)+'\n'
    k = int(infile.readline().split(' ')[0])
    result = ''
    for j in range(k):
        result += ' '
        result += str(j+1)
    
    ofile.write('Case #'+str(i+1)+':'+result+'\n')


ofile.close()