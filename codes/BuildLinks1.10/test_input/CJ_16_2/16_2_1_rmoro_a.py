#//////////////////////////////////////////////////////////////////
# AUTHOR:   Robert Morouney <069001422>
# EMAIL:    robert@morouney.com 
# FILE:     a.py
# CREATED:  2016-04-30 12:41:17
# MODIFIED: 2016-04-30 14:04:34
#//////////////////////////////////////////////////////////////////

fin = open ( 'in', 'r' )
fout = open ('out', 'w' )

n_cases = int(fin.readline().strip())
for case in range ( n_cases ):
    string = fin.readline().strip()
    n_phone = list()
    for _ in range (10000):
        if 'W' in string:
            string = string.replace('T','',1)
            string = string.replace('W','',1)
            string = string.replace('O','',1)
            n_phone.append('2')
        if 'U' in string:
            string = string.replace('F','',1)
            string = string.replace('O','',1)
            string = string.replace('U','',1)
            string = string.replace('R','',1)
            n_phone.append('4')
        if 'X' in string:
            string = string.replace('S','',1)
            string = string.replace('I','',1)
            string = string.replace('X','',1)
            n_phone.append('6')
        if 'G' in string:
            string = string.replace('E','',1)
            string = string.replace('I','',1)
            string = string.replace('G','',1)
            string = string.replace('H','',1)
            string = string.replace('T','',1)
            n_phone.append('8')
        if 'Z' in string:
            string = string.replace('Z','',1)
            string = string.replace('E','',1)
            string = string.replace('R','',1)
            string = string.replace('O','',1)
            n_phone.append('0')
    for _ in range (10000):
        if 'H' in string:
            string = string.replace('T','',1)
            string = string.replace('H','',1)
            string = string.replace('R','',1)
            string = string.replace('E','',1)
            string = string.replace('E','',1)
            n_phone.append('3')
        if 'F' in string:
            string = string.replace('F','',1)
            string = string.replace('I','',1)
            string = string.replace('V','',1)
            string = string.replace('E','',1)
            n_phone.append('5')
        if 'O' in string:
            string = string.replace('O','',1)
            string = string.replace('N','',1)
            string = string.replace('E','',1)
            n_phone.append('1')
    for _ in range(10000):    
        if 'V' in string:
            string = string.replace('S','',1)
            string = string.replace('E','',1)
            string = string.replace('V','',1)
            string = string.replace('E','',1)
            string = string.replace('N','',1)
            n_phone.append('7')
        if 'N' in string:
            string = string.replace('N','',1)
            string = string.replace('I','',1)
            string = string.replace('N','',1)
            string = string.replace('E','',1)
            n_phone.append('9')
    if string == '': print 'SUCCESS!'
    pstring = ''.join(sorted(n_phone))
    
    print "Case #{}: {}".format(case+1,pstring)
    fout.write("Case #{}: {}\n".format(case+1,pstring))
    
fin.close()
fout.close()
