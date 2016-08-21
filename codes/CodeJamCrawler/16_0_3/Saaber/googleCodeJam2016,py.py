basePow = [[pow(b, i) for i in xrange(33)] for b in xrange(11)]
numInBase = {}
divisorDic = {}

def checkPrime(n):
    return True

def findDivisor(n):
    if n in divisorDic:
        return divisorDic[n]
    d = 2
    while d * d <= n:
        if n % d == 0:
            divisorDic[n] = d
            return d
        d += 1
    divisorDic[n] = None
def getJnonPrimesN(N, J):
    res = []
    n = -1
    while len(res) < J:
        n += 1
        nextNumBinString = bin(n)[2:]
        isPrime = True
        divisorsInBase = []
        for b in xrange(2,11):
            nextNumVal = 0
            if (n, b) not in numInBase:
                i = len(nextNumBinString) - 1
                power = 1
                while i >= 0:
                    if nextNumBinString[i] == '1':
                        nextNumVal += basePow[b][power]
                    i = i - 1
                    power += 1
                numInBase[(n,b)] = nextNumVal
                nextNumVal += (1 + basePow[b][N-1])
            else:
                nextNumVal = numInBase[(n,b)] + 1 +  basePow[b][N-1]
            #print 'nexNumVal:',nextNumVal, 'b:', b,'nextNumBinString:','1'+'0'*(N - 2 - len(nextNumBinString))+nextNumBinString+'1', "basePow[b][N-1]:",basePow[b][N-1]
            divisor = findDivisor(nextNumVal)
            if not divisor:
                isPrime = False
                break
            else:
                divisorsInBase.append(str(divisor))
        if isPrime and nextNumVal > 0:
            res.append(('1'+'0'*(N - 2 - len(nextNumBinString))+nextNumBinString+'1', divisorsInBase))
    return res

fin = open('inputFile.in', 'r')
fout = open('outputFile.out', 'w')
T = int(fin.readline().strip())

for t in xrange(T):
    line = fin.readline().strip()
    args = [int(arg) for arg in line.split() if arg != '' and arg != '\n']
    res = getJnonPrimesN(args[0], args[1])
    fout.write('Case #'+str(t+1)+':\n')
    for r in res:
        fout.writelines(str(r[0])+' '+' '.join(r[1])+'\n')

fin.close()
fout.close()

                
            
                
            
