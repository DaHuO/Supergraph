from math import sqrt
def gen_prime(N):
    res = []
    for num in range(2,N + 1):
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            res.append(num)
    return res
def is_prime(N,primes):
    sqN = sqrt(N)
    prime = list(primes)
    prime.append(sqN)
    prime.sort()
    ind = prime.index(sqN)
    prime = primes[0:ind+1]
    is_p = True
    div = None
    for p in prime:
        if N%p==0:
            is_p = False
            div = p
            break
    return is_p,div

def toDecimal(b,base):
    res = 0
    b = list(b)
    b.reverse()
    for i in range(len(b)):
        if b[i]=='1':
            res += pow(base,i)
    return res

def find_J(N,J):
    start = pow(2,N-1) + 1
    res = []
    current = start
    end = pow(2,N) -1
    primes = gen_prime(pow(2,15))
    while(current<=end):
        divisors = []
        is_p,p = is_prime(current,primes)
        if is_p:
            current += 2
            continue
        divisors.append(p)
        b = bin(current)[2:]
        good = True
        for base in range(3,11):
            temp = toDecimal(b,base)
            is_p,p = is_prime(temp,primes)
            if is_p:
                good = False
                break
            divisors.append(p)
        if good:
            res.append((b,divisors))
            if len(res) ==J:
                break
        current += 2
    out = open('C-large.out','w')
    out.write('Case #1:\n')
    for r in res:
        out.write(r[0]+' '+' '.join(map(str,r[1]))+'\n')
    out.close()
    return res

if __name__=='__main__':
    res = find_J(32,500)
    assert len(res) == 500
