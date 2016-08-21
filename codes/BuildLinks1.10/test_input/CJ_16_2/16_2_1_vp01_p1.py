test=input()


ll = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
for i in xrange(test):
    nn = list(raw_input())

    
    #result = []

    noz=no1=no2=no3=no4=no5=no6=no7=no8=no9=0
    noz=nn.count('Z')
    
    
    for k in xrange(noz):
        nn.remove('Z')
        nn.remove('E')
        nn.remove('R')
        nn.remove('O')
    
    no6 = nn.count('X')
    for k in xrange(no6):
        nn.remove('S')
        nn.remove('I')
        nn.remove('X')

    no2=nn.count('W')
    for k in xrange(no2):
        nn.remove('T')
        nn.remove('W')
        nn.remove('O')

    no4=nn.count('U')
    for k in xrange(no4):
        nn.remove('F')
        nn.remove('O')
        nn.remove('U')
        nn.remove('R')

    no8=nn.count('G')
    for k in xrange(no8):
        nn.remove('E')
        nn.remove('I')
        nn.remove('H')
        nn.remove('G')
        nn.remove('T')

    no1=nn.count('O')

    
    
    
    for k in xrange(no1):
        nn.remove('O')
        nn.remove('N')
        nn.remove('E')
    no3=nn.count('T')
    for k in xrange(no3):
        nn.remove('T')
        nn.remove('H')
        nn.remove('R')
        nn.remove('E')
        nn.remove('E')

    no5=nn.count('F')
    for k in xrange(no5):
        nn.remove('F')
        nn.remove('I')
        nn.remove('V')
        nn.remove('E')
        
    
    no7=nn.count('S')
    for k in xrange(no7):
        nn.remove('E')
        nn.remove('S')
        nn.remove('V')
        nn.remove('E')
        nn.remove('N')
    
    no9=nn.count('I')
    for k in xrange(no9):
        nn.remove('N')
        nn.remove('I')
        nn.remove('N')
        nn.remove('E')

    result=('0'*noz)+('1'*no1)+('2'*no2)+('3'*no3)+('4'*no4)+('5'*no5)+('6'*no6)+('7'*no7)+('8'*no8)+('9'*no9)
    print "Case #%d: %s"%(i+1,result)

    
