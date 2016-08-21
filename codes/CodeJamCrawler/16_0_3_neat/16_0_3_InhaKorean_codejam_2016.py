FILE_PATH = 'C:\\codejam\\'
FILE_NAME = 'C-large'

f = open(FILE_PATH + FILE_NAME + '.in', 'r')
o = open(FILE_PATH + FILE_NAME + '.out', 'w')

MP = 10000000
MAX_N = 32
MAX_J = 500
def generatePrime() :
    L = [True]*(MP+1)
    L[0] = L[1] = False
    for i in range(2, MP+1) :
        if L[i] :
            for j in range(i*2, MP+1, i) :
                L[j] = False
    S = set()
    for i in range(2, MP+1) :
        if L[i] : 
            S.add(i)
    return S

Prime = generatePrime()
Prime_L = sorted(Prime)
#print('Prime generated (' +str(len(Prime)) + ')')

def isPrime(n) :
    if n <= Prime_L[-1] :
        return n in Prime
    for i in Prime_L :
        if i*i > n :
            return True
        if n % i == 0 : return False
    '''
    i = Prime_L[-1]
    while i*i <= n :
        if n % i == 0 :
            return False
        else :
            i += 2
    '''
    return True

def proveJamcoin(x) :
    ret = x + ' '
    for i in range(2, 10) :
        n = int(x, base = i)
        for p in Prime_L :
            if n % p == 0 :
                ret += str(p) + ' '
                break
    n = int(x)
    for p in Prime_L :
        if n % p == 0 :
            ret += str(p)
            break
    return ret

def case_result(case) :
    L = [set() for i in range(MAX_N+1)]
    for i in range(4, MAX_N+1) :##
        for j in range(2**(i-1) + 1, 2**i, 2) :
            s = bin(j)[2:]
            if s in L[i] : continue
            for k in range(2, 11) :
                if k == 10 and isPrime(int(s)) :
                    break
                if isPrime(int(s, base = k)) :
                    break
            else :
                L[i].add(s)
                
                for k in range(i*2, MAX_N+1) :
                    s2 = s+'0'*(k-2*i)+s
                    L[len(s2)].add(s2)
                    if k % i == 0 :
                        s2 = s*(k//i)
                        L[len(s2)].add(s2)
                
            if len(L[i]) >= MAX_J :
                break

        #print(i, len(L[i]))
    #print('input:')
    #N,J = map(int, input().split())
    N,J = map(int, f.readline().split())
    
    ret = ''
    R = list(L[N])
    for i in range(J) :
        ret += proveJamcoin(R[i])
        if i != J-1 :
            ret += '\n'
    return ret
T = int(f.readline())
#T = int(input())
for case in range(1, T+1) :
    o.write('Case #'+str(case)+':\n'+case_result(case)+'\n')
 
f.close()
o.close()
 