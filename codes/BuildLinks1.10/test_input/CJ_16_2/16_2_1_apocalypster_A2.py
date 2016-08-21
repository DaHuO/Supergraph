f = open("Alarge.in",'r')
digits = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
# exclusives: 0 - z, 2 - w, 4 - u, 6 - x, 8 - g
t = int(f.readline().strip())
for j in range(t):
    s = f.readline().strip()
    slist = []
    for c in s:
        slist.append(c)
    slist.sort()
    currentdigits = []
    i = 0
    for k in range(slist.count('Z')):
        currentdigits.append('0')
        slist.remove('Z')
        slist.remove('E')
        slist.remove('R')
        slist.remove('O')

    for k in range(slist.count('W')):
        
        currentdigits.append('2')
        slist.remove('T')
        slist.remove('W')
        slist.remove('O')

    for k in range(slist.count('U')):
        currentdigits.append('4')
        slist.remove('F')
        slist.remove('U')
        slist.remove('R')
        slist.remove('O')

    for k in range(slist.count('X')):
        currentdigits.append('6')
        slist.remove('S')
        slist.remove('I')
        slist.remove('X')

    for k in range(slist.count('G')):
        currentdigits.append('8')
        slist.remove('E')
        slist.remove('I')
        slist.remove('G')
        slist.remove('H')
        slist.remove('T')

    for k in range(slist.count('O')):
        currentdigits.append('1')
        slist.remove('O')
        slist.remove('N')
        slist.remove('E')

    for k in range(slist.count('F')):
        currentdigits.append('5')
        slist.remove('F')
        slist.remove('I')
        slist.remove('V')
        slist.remove('E')

    for k in range(slist.count('V')):
        currentdigits.append('7')
        slist.remove('E')
        slist.remove('S')
        slist.remove('V')
        slist.remove('E')
        slist.remove('N')

    for k in range(slist.count('T')):
        currentdigits.append('3')
        slist.remove('E')
        slist.remove('T')
        slist.remove('H')
        slist.remove('E')
        slist.remove('R')

    for k in range(slist.count('E')):
        currentdigits.append('9')
        slist.remove('N')
        slist.remove('I')
        slist.remove('N')
        slist.remove('E')

    currentdigits.sort()
    
    
            

    print "Case #" + str(j+1) + ": " + ''.join(currentdigits)

f.close()
