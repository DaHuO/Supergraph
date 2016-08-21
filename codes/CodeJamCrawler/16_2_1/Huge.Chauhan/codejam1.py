t = int(input())
for i in range(1,t+1):
    num = ''
    s = list(input())
    while s != []:
        if 'Z' in s:
            num+='0'
            s.remove('Z')
            s.remove('E')
            s.remove('R')
            s.remove('O')
        elif 'W' in s:
            num+='2'
            s.remove('T')
            s.remove('W')
            s.remove('O')        
        elif 'U' in s :
            num+='4'
            s.remove('F')
            s.remove('U')
            s.remove('O')
            s.remove('R')        
        elif 'X' in s:
            num+='6'
            s.remove('S')
            s.remove('I')
            s.remove('X')       
        elif 'G' in s:
            num+='8'
            s.remove('E')
            s.remove('I')
            s.remove('G')
            s.remove('H')
            s.remove('T')
        elif 'O' in s  :
            num+='1'
            s.remove('O')
            s.remove('N')
            s.remove('E')
        elif 'H' in s :
            num+='3'
            s.remove('T')
            s.remove('H')
            s.remove('R')
            s.remove('E')
            s.remove('E')
        elif 'S' in s :
            num+='7'
            s.remove('S')
            s.remove('E')
            s.remove('V')
            s.remove('E')
            s.remove('N')    
        elif 'F' in s :
            num+='5'
            s.remove('F')
            s.remove('I')
            s.remove('V')
            s.remove('E')        
        else:
            num+='9'
            s.remove('N')
            s.remove('I')
            s.remove('N')
            s.remove('E') 
    ans = sorted([int(x) for x in num])
    k = [str(z) for z in ans]
    final = ''.join(k)
    print("Case #%d: %s" %(i,final))
