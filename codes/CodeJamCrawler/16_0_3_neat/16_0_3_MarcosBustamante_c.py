import math


n, j, c = 16, 50, 0
primos = []

def euler():
    vet = [0] * (2**n+1)
    vet[0] = vet[1] = 1
    
    m = 2**(n/2);
    for i in range(2, m+1):
        if not vet[i]:
            for k in range(i*i, 2**n+1, i):
                vet[k] = 1
    
    for i in range(2**n+1):
        if not vet[i]:
            primos.append(i)

euler()
ini = (2**(n-1))+1
fim = (2 ** n) - 1

print 'Case #1:'
while ini <= fim and c < j:
    b = bin(ini)
    bstr = b[2:]
    if not(bstr[0] == '1' and bstr[-1] == '1'):
        continue
    else:
        ok, result = True, []
        for x in xrange(2, 11):
            n = int(bstr, x)
            if n in primos:
                ok = False
                break
            else:
                result.append(str(n))
        if ok:
            print bstr, ' '.join(result)
            c += 1
    ini += 2
