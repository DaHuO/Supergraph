
import math

# Senate

# 2016 1C A

inp = open('senate_input.txt')
outp = open('senate_output.txt', 'w')

lines = inp.readlines()

cases = int(lines[0])

# print (cases)

fact_table = {}

def get_factor(nr):
    return 1

ind1 = 1

for c in range (0, cases):
    case = lines[ind1]
    ind1 = ind1 + 1
#    print (c, '->', case, end='')
    line = case[:-1].split(' ')

    outp.write ("Case #{0}: ".format(c+1))
    
#    print (line)
#    print ("Case #{0}: ".format(c+1), end='')

    case = lines[ind1]
    line = case[:-1].split(' ')
    ind1 = ind1 + 1

    line = [int(p) for p in line]

    # we werken met LINE
    
#    print (str(line))
    t = len(line)

    # find max and index of it
    m = max (line)
    s = []
    q = m*t-sum(line);

    while q>0:
        mi = line.index(m)
        line[mi] = line[mi]-1
        m = max (line)
        q = m*t-sum(line)
        s.append (chr(mi + ord('A')))

    while m>0:
        for i in range(2, t):
            s.append (chr(i + ord('A')))
        s.append('AB')
        m = m-1

#    print(s)
    outp.write (' '.join(s));
    outp.write ('\n')

inp.close()
outp.close()

# print ('** Program finished **')
