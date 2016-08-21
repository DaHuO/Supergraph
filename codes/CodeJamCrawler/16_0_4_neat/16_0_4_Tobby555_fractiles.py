import math

# Fractiles

# 2016 Qualifier 4

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

    # we werken met LINE
    
    k = line[0]
    c = line[1]
    s = line[2]

#    print (k,c,s)

    if (c==1):
        if (s<k):
            # print ('IMPOSSIBLE')
            outp.write ('IMPOSSIBLE')
        else:
            for i in range (1,k):
                 # print (i, end=' ')
                 outp.write (str(i) + ' ')
            # print (k)
            outp.write (str (k))
    else:
        if (s < k/2):
            # print ('IMPOSSIBLE')
            outp.write ('IMPOSSIBLE')
        else:
            for i in range (0, math.floor(k/2)):
                 # print (i*(2*k + 2) + 2, end=' ')
                 outp.write (str (i*(2*k + 2) + 2) + ' ')
            if k%2 > 0:
                # print (k)
                outp.write (str(k))
            # else:
                # print ()

# TODO

    outp.write ('\n')

inp.close()
outp.close()

# print ('** Program finished **')
