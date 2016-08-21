t=input()
#d={'Z':'0','W':'2','X':'6','G';'8','U':'4',}
case=1
while t:
    t=t-1
    s=list(raw_input())
    l=[]
    while 'Z' in s:
        l.append('0')
        s.remove('Z');
        s.remove('E');
        s.remove('R');
        s.remove('O');
    while 'W' in s:
        l.append('2')
        s.remove('T')
        s.remove('W')
        s.remove('O')
    while 'X' in s:
        l.append('6')
        s.remove('S')
        s.remove('I')
        s.remove('X')
    while 'G' in s:
        l.append('8')
        s.remove('E')
        s.remove('I')
        s.remove('G')
        s.remove('H')
        s.remove('T')
    while 'U' in s:
        l.append('4')
        s.remove('F')
        s.remove('O')
        s.remove('U')
        s.remove('R')
    while ('O' in s) and ('N' in s) and ('E' in s):
        l.append('1')
        s.remove('O')
        s.remove('N')
        s.remove('E')
    
    while 'H' in s:
        l.append('3')
        s.remove('T')
        s.remove('H')
        
        s.remove('R')
        s.remove('E')
        s.remove('E')
    
    while 'F' in s:
        l.append('5')
        s.remove('F')
        s.remove('I')
        s.remove('V')
        s.remove('E')
    while 'V' in s:
        l.append('7')
        s.remove('S')
        s.remove('E')
        s.remove('V')
        s.remove('E')
        s.remove('N')
    while (s.count('N')>=2) and ('I' in s) and ('E' in s):
        l.append('9')
        s.remove('N')
        s.remove('I')
        s.remove('N')
        s.remove('E')
    l.sort()
    l=''.join(l)
    print "Case #%d: %s"% (case,l)
    case+=1
    
    

 
    
        
    
