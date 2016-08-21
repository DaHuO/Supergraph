import sys
import math

t,n,j = open('C-small-attempt0.in').read().split()
n = int(n)
j = int(j)
coins = 0
divs = []
i = int('1' + ('0' * (n-2)) + '1', 2)
outFile = open('a.out','w')

def str_base(num, base):
    if base < 2:
        return 'False'
    d,m = divmod(num, base)
    if d == 0:
        return str(m)
    return str_base(d, base) + str(m)

def factor(num):
    if num < 2:
        return False
    return next((z for z in range(2, math.ceil(math.sqrt(num) ) + 1 ) if num%z == 0), False) 

outFile.write('Case #1:\n')
print('Case #1:')

for index in range(j):
    while coins < index + 1:
        if len(str_base(i,2)) > n:
            break
        del divs[:]
        for k in range(2,11):
            temp = int(str_base(i,2), k)
            f = str(factor(temp))
            if f == 'False':
                break
            divs.append(f)
        if len(divs) == 9:        
            output = str_base(i,2)
            for d in divs:
                output += ' ' + d
            outFile.write(output + '\n')
            print(output)
            coins += 1
        i += 2
        


      