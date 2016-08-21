import math

# Counting Sheep

# 2016 Qualifier 1

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
    line = [int(p) for p in line]
    n = line[0]
    p = n

    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if (n==0):
#        print ("INSOMNIA")
        outp.write ("INSOMNIA")
    else:
        while (len(l)>0):
            m = []
            for x in l:
                if not (x in str(p)):
                    m.append (x)
            # print (p, m)
            p = p+n
            l = m
        p = p-n
#        print (p)
        outp.write (str(p))
                
# TODO

    outp.write ('\n')

inp.close()
outp.close()

# print ('** Program finished **')
