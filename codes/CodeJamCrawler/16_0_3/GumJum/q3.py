
import sys

from math import sqrt, ceil

def getDiv(n):
    for i in range(3, int(sqrt(n)) + 1):
        if (n % i == 0):
            return i
    return -1

def checkAllDivs(n):
    l = []
    for i in range(2, 11):
        a = getDiv(int(n, i))
        if (a == -1):
            return []
        l.append(a)
    return l
    
def genStr(n, l):
    s = ''
    b = bin(n)
    s += b[2:] + ' '
    for x in l:
        s += str(x) + ' '
    return s[:-1]
    
def getTest(N, J):
    s = ''
    n = 2 ** (N - 1) - 1
    l = []
    for i in range(J):
        print 'i=' + str(i)
        check = False
        while not check:
            n += 2
            b = bin(n)
            l = checkAllDivs(b[2:])
            check = len(l) != 0
        s += genStr(n,l) + '\n'
    return s

def main():
    to_write = ''
    with open(sys.argv[1], 'r') as f:
        first_line = f.readline()
        count = 0
        
        for l in f:
            count += 1
            args = l.strip().split(' ')
            s = getTest(int(args[0]), int(args[1]))
            to_write += 'Case #' + str(count) + ':\n' + s
    
    with open(sys.argv[2], 'w') as f:
        f.write(to_write)
        
if __name__ == '__main__':
    #print getTest(15, 60)
    main()