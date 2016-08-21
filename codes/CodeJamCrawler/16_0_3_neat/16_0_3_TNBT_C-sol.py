def seq(N,i=0,imax=0):
    while i < imax:
        yield ('0'*N+bin(i)[2:])[-N:]
        i += 1

def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

for _ in range(int(input())):
    N,J = map(int,raw_input().split())

    primes = []
    for prime in gen_primes():
        # if prime >= ((2**N)-1):
        if prime >= N**2:
            break
        primes.append(prime)

    print('Case #{}:'.format(_+1))
    for i in seq(N-2,0,2**(N-2)):
        L = []
        for base in range(2,11):
            divFound = False
            for prime in primes:
                if int('1'+i+'1',base)%prime == 0:
                    L.append(prime)
                    divFound = True
                    break
            else:
                divFound = False

            if not divFound:
                break
        else:
            J-=1
            print '1'+i+'1',
            for i in L:
                print i,
            print ''
            if J == 0:
                break