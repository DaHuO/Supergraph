fi=open("A-large.in",'r')
fo=open("output(2).txt",'w')

for i in range(int(fi.readline().strip())):
    r=fi.readline().strip()
    s=[]
    for c in r:
        s.append(c)
    print 'here'
    a=[]
    while 'Z' in s:
        a.append('0')
        s.remove('Z')
        s.remove('E')
        s.remove('R')
        s.remove('O')
    while 'X' in s:
        a.append('6')
        s.remove('S')
        s.remove('I')
        s.remove('X')        
        
    while 'V'in s and 'S' in s :
        a.append('7')
        s.remove('S')
        s.remove('E')
        s.remove('V') 
        s.remove('E')
        s.remove('N')
    
    while 'V' in s:
        a.append('5')
        s.remove('F')
        s.remove('I')
        s.remove('V')
        s.remove('E')
    
    while 'F' in s:
        a.append('4')
        s.remove('F')
        s.remove('O')
        s.remove('U')
        s.remove('R')
        
    while 'W' in s:
        a.append('2')
        s.remove('T')
        s.remove('W')
        s.remove('O')
    
    while 'O' in s:
        a.append('1')
        s.remove('O')
        s.remove('N')
        s.remove('E')
    
    while 'N' in s:
        a.append('9')
        s.remove('N')
        s.remove('I')
        s.remove('N')
        s.remove('E')   
        
    while 'R' in s:
        a.append('3')
        s.remove('T')
        s.remove('H')
        s.remove('R')
        s.remove('E')        
        s.remove('E')
    
    while 'I' in s:
        a.append('8')
        s.remove('E')
        s.remove('I')
        s.remove('G')
        s.remove('H')        
        s.remove('T')
        
        
        
    ans=''.join(sorted(a))
  
    fo.write("Case #%d: %s\n" %(i+1,ans))