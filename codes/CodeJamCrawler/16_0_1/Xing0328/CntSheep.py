# code for counting sheep

infile = open("A-large.in",'r')
casenum = int(infile.readline())


ofile = open('A-large.txt','w')

for i in range(casenum):
    print 'Case #'+str(i+1)+'--------------'
    digList = ['0','1','2','3','4','5','6','7','8','9']
    num = int(infile.readline())
   
    if num == 0:
        result = 'INSOMNIA'
        ofile.write('Case #'+str(i+1)+': '+result+'\n')
    else: 
        tempNum = 0 
        
        while (len(digList) != 0):
            tempNum += num
            numstr = str(tempNum)
           
            for char in numstr:
                if (char in digList):
                    digList.remove(char)
        
        result = numstr 
        
        ofile.write('Case #'+str(i+1)+': '+result+'\n')

ofile.close()