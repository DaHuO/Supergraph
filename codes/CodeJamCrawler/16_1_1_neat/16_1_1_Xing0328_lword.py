infile = open("A-large.in",'r')
casenum = int(infile.readline())


ofile = open('A-large.txt','w')

for i in range(casenum):
    print 'Case #'+str(i+1)+'--------------'
    s = infile.readline().split('\n')[0]
    
    res = s[0]
    for ind in range(1,len(s)):
        if s[ind] >= res[0]:
            res = s[ind] + res
            
        else:
            res = res + s[ind]
    
    
    ofile.write('Case #'+str(i+1)+': '+res+'\n')

ofile.close()