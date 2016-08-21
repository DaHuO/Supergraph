def tillAllDigits(N):
    if N == 0:
        return 'INSOMNIA'
    l = len(str(N))
    digits = {}
    for coeff in xrange(1,10000000):
        n = coeff * N
        sn = str(n)
        for d in sn:
            if n not in digits:
                digits[d] = 1
        if len(digits) == 10:
            return n
##    for i in xrange(1,9):
##        n = pow(10,l)*N + pow(10,l)*i
##        sn = str(n)
##        for d in sn:
##            if n not in digits:
##                digits[d] = 1
##        if len(digits) == 10:
##            return n
##    return 'INSOMNIA'

fin = open('inputFile.in', 'r')
fout = open('outputFile.out', 'w')
T = int(fin.readline().strip())

for t in xrange(T):
    line = fin.readline().strip()
    args = [int(arg) for arg in line.split() if arg != '' and arg != '\n']
    minNum = tillAllDigits(args[0])
    fout.write('Case #'+str(t+1)+': ' + str(minNum)+'\n')

fin.close()
fout.close()
