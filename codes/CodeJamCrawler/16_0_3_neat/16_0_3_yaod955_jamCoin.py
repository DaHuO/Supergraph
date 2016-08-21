import sys

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]

cases = ['Case #1:\n']
n = int(sys.argv[2])
j = int(sys.argv[3])

def checkJC(val):
    divisors = ''
    for i in range(2,11):
        x = 0
        hasDiv = False
        for b in val:
            x *= i
            x += int(b)
        for p in primes:
            if (x%p==0):
                hasDiv = True
                divisors += ' '+str(p)
                break
        if(not hasDiv):
            return
    cases.append(val+divisors+'\n')

def findJC(val,d):
    if (len(cases)<j+1):
        if (d == 1):
            checkJC(val+'1')
        else:
            findJC(val+'0',d-1)
            findJC(val+'1',d-1)

findJC('1',n-1)
print(len(cases)-1)

with open(sys.argv[1],'w+') as g:
    g.writelines(cases)
#             