file = open('D-small-attempt1.in','r')
total = int(file.readline())
for i in range(1,total+1):

    input = file.readline()
    K = int(input.split()[0])
    C = int(input.split()[1])
    S = int(input.split()[2]) 
    
    
    pos = range(1,S+1)
    res = ''
    for p in pos: res=res+str(p)+' '
    print 'case #%d: %s' % (i,res)
       
    
