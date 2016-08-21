test = input()

for g in xrange(test):

    s = raw_input()
    s = list(s)
    ans = []
    
    while(1):
        if 'Z' in s:
            ans.append('0')
            s.remove('Z')
            s.remove('E')
            s.remove('R')
            s.remove('O')
        else:
            break

    while(1):
        if 'W' in s:
            ans.append('2')
            s.remove('T')
            s.remove('W')
            s.remove('O')
        else:
            break

    while(1):
        if 'U' in s:
            ans.append('4')
            s.remove('F')
            s.remove('O')
            s.remove('U')
            s.remove('R')
        else:
            break

    while(1):
        if 'X' in s:
            ans.append('6')
            s.remove('S')
            s.remove('I')
            s.remove('X')
        else:
            break

    while(1):
        if 'G' in s:
            ans.append('8')
            s.remove('E')
            s.remove('I')
            s.remove('G')
            s.remove('H')
            s.remove('T')
        else:
            break
    
    while(1):
        if 'O' in s:
            ans.append('1')
            s.remove('E')
            s.remove('N')
            s.remove('O')
        else:
            break
            
    while(1):
        if 'S' in s:
            ans.append('7')
            s.remove('E')
            s.remove('E')
            s.remove('V')
            s.remove('S')
            s.remove('N')
        else:
            break
            
    while(1):
        if 'R' in s:
            ans.append('3')
            s.remove('E')
            s.remove('E')
            s.remove('R')
            s.remove('H')
            s.remove('T')
        else:
            break

    while(1):
        if 'F' in s:
            ans.append('5')
            s.remove('F')
            s.remove('I')
            s.remove('V')
            s.remove('E')
        else:
            break

    for x in xrange(int(len(s)/4)):
            ans.append('9')
    ans.sort()
    print "Case #"+ str(g+1) + ': ' + ''.join(ans)
