# pancake 

infile = open("B-large.in",'r')
casenum = int(infile.readline())
ofile = open('B-large.txt','w')

for i in range(casenum):
    print 'Case #'+str(i+1)+'\n'
    
    cond = infile.readline().split('\n')[0]
    print len(cond)
    result = 0
    for j in range(len(cond)-1):
       if(cond[j] != cond[j+1]):
           result +=1
    if cond[-1] == '-':
        result += 1
     
    ofile.write('Case #'+str(i+1)+': '+str(result)+'\n')




ofile.close()