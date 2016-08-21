import math
from collections import Counter

# Counting the digits

# 2016 1B 1

def parse_1(l):
    p = [ 0,0,0,0,0,0,0,0,0,0 ];
    
    x = l['Z']
    p[0] = x
    l['Z']=0
    l['E']=l['E']-x
    l['R']=l['R']-x
    l['O']=l['O']-x
    
    x = l['W']
    p[2] = x
    l['W']=0
    l['T']=l['T']-x
    l['O']=l['O']-x
    
    x = l['U']
    p[4] = x
    l['U']=0
    l['F']=l['F']-x
    l['O']=l['O']-x
    l['R']=l['R']-x

    x = l['X']
    p[6] = x
    l['X']=0
    l['I']=l['I']-x
    l['S']=l['S']-x

    x = l['G']
    p[8] = x
    l['G']=0
    l['E']=l['E']-x
    l['I']=l['I']-x
    l['H']=l['H']-x
    l['T']=l['T']-x

    x = l['O']
    p[1] = x
    l['O']=0
    l['E']=l['E']-x
    l['N']=l['N']-x

    x = l['T']
    p[3] = x
    l['T']=0
    l['E']=l['E']-x
    l['E']=l['E']-x
    l['H']=l['H']-x
    l['R']=l['R']-x

    x = l['F']
    p[5] = x
    l['F']=0
    l['E']=l['E']-x
    l['I']=l['I']-x
    l['V']=l['V']-x

    x = l['S']
    p[7] = x
    l['S']=0
    l['E']=l['E']-x
    l['E']=l['E']-x
    l['V']=l['V']-x
    l['N']=l['N']-x

    x = l['I']
    p[9] = x
    l['I']=0

    q = "";
    for i in range(0,10):
        for j in range(0,p[i]):
            q = q+str(i)
    
    return q
    


inp = open('digit_input.txt')
outp = open('digit_output.txt', 'w')

lines = inp.readlines()

cases = int(lines[0])

# print (cases)

ind1 = 1

for c in range (0, cases):
    case = lines[ind1]
    ind1 = ind1 + 1
#    print (c, '->', case, end='')
    line = case[:-1].split(' ')

    outp.write ("Case #{0}: ".format(c+1))
    
#    print (line)
#    print ("Case #{0}: ".format(c+1), end='')

    line = case[:-1].split(' ')
#    line = [int(p) for p in line]

    # we werken met LINE
    
    line = line[0]
#    print (line)

    linelist = Counter(list(line))
#    print (linelist)
    r = parse_1(linelist)
#    print (r);

    outp.write (str(r))
               
# TODO

    outp.write ('\n')

inp.close()
outp.close()

# print ('** Program finished **')
