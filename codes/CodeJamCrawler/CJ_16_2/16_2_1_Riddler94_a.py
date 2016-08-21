inp = open("A-large.in" , 'r')
out = open("A-large-out.txt", 'w')

for case in range(int(inp.next())):
    s = list(inp.next())
    s.sort()
    s.reverse()
    res = []
    while('Z' in s):
        s.remove('Z')
        s.remove('E')
        s.remove('R')
        s.remove('O')
        res.append('0')
    
    while('W' in s):
        s.remove('T')
        s.remove('W')
        s.remove('O')
        res.append('2')

    while('X' in s):
        s.remove('S')
        s.remove('I')
        s.remove('X')
        res.append('6')
        
    while('U' in s):
        s.remove('F')
        s.remove('O')
        s.remove('U')
        s.remove('R')
        res.append('4')
        
    while('G' in s):
        s.remove('E')
        s.remove('I')
        s.remove('G')
        s.remove('H')
        s.remove('T')
        res.append('8')

    while('H' in s):
        s.remove('T')
        s.remove('H')
        s.remove('R')
        s.remove('E')
        s.remove('E')
        res.append('3')

    while('F' in s):
        s.remove('F')
        s.remove('I')
        s.remove('V')
        s.remove('E')
        res.append('5')
        
    while('S' in s):
        s.remove('S')
        s.remove('E')
        s.remove('V')
        s.remove('E')
        s.remove('N')
        res.append('7')

    while('I' in s):
        s.remove('N')
        s.remove('I')
        s.remove('N')
        s.remove('E')
        res.append('9')
        
    while('O' in s):
        s.remove('O')
        s.remove('N')
        s.remove('E')
        res.append('1')

    res.sort()
    ph = ''.join(res)
    out.write("Case #%d: %s\n" % (case+1, ph))

inp.close()
out.close()
