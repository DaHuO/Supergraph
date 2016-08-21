




for z in range(int(input())):
    
    s=input()
    s=list(s)
    a=""
    while(len(s)!=0):
        if 'Z' in s:
            s.remove('Z')
            s.remove('E')
            s.remove('R')
            s.remove('O')
            a+="0"
        elif 'W' in s:
            s.remove('T')
            s.remove('W')
            s.remove('O')
            a+="2"
        elif 'U' in s:
            s.remove('F')
            s.remove('O')
            s.remove('U')
            s.remove('R')
            a+="4"
        elif 'X' in s:
            s.remove('S')
            s.remove('I')
            s.remove('X')
            a+="6"
        elif 'G' in s:
            s.remove('E')
            s.remove('I')
            s.remove('G')
            s.remove('H')
            s.remove('T')            
            a+="8"
        elif 'O' in s:
            s.remove('O')
            s.remove('N')
            s.remove('E')
            a+="1"
        elif 'R' in s:
            s.remove('T')
            s.remove('H')
            s.remove('R')
            s.remove('E')
            s.remove('E')            
            a+="3"
        elif 'F' in s:
            s.remove('F')
            s.remove('I')
            s.remove('V' )
            s.remove('E')
            a+="5"
        elif 'S' in s:
            s.remove('S')
            s.remove('E')
            s.remove('V')
            s.remove('E')
            s.remove('N')            
            a+="7"
        else:
            s.remove('N')
            s.remove('I')
            s.remove('N')
            s.remove('E')
            a+="9"
            
            
        a="".join(sorted(a))    
            
            
            
            
    print ("Case#{} {}".format(z+1,a))