import math

# Revenge of the Pancakes

# 2016 Qualifier 2

inp = open('input.txt')
outp = open('output.txt', 'w')

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

    r = 0

    if line[0]=='-':
        r = 1

    for i in range(1, len(line)):
        if (line[i]=='-') and (line[i-1]=='+'):
            r = r + 2

    outp.write (str(r))
               
# TODO

    outp.write ('\n')

inp.close()
outp.close()

# print ('** Program finished **')
