
import math

# Coinjam

# 2016 Qualifier 3

inp = open('input.txt')
outp = open('output.txt', 'w')

lines = inp.readlines()

cases = int(lines[0])

# print (cases)

fact_table = {}

def get_factor(nr):
    if nr in fact_table:
        return fact_table[i]
    
    # for i in range (2,math.floor(math.sqrt(nr))):
    # instead we give up at 100k :P
    
    for i in range (2,100000):
        if ((nr%i) == 0):
            fact_table[nr] = i
            return i
    
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

    line = case[:-1].split(' ')
    line = [int(p) for p in line]

    # we werken met LINE
    
    n = line[0]
    j = line[1]
    outp.write ('\n')

    i = 0
    xx = 0
    form = '{0:0' + str(n-2) + 'b}'
    while (i<j):
        x = form.format(xx)
        x = '1' + x + '1'
        # print (x, end = ' ')

        res = []
        for p in range (2,11):
            y = int (x, p)
            # print (y, end = ' ')

            tt = get_factor(y)
            if (tt != 1):
                res.append(tt)
            else:
                # print ()
                # print (y, tt)
                break

        if len(res)==9:
            # print (y, ' '.join(map(str, res)))
            outp.write (x + ' ' + ' '.join(map(str, res)))
            outp.write ('\n')
            i = i + 1

        # print()
        xx = xx + 1

    # outp.write (str(r))
               
# TODO

    # outp.write ('\n')

inp.close()
outp.close()

# print ('** Program finished **')
