def primes(n) :
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

P = primes(10**6)

f = open('res.in')
g = open('res.out', 'w')

T = int(f.readline()[:-1])

for case in range(T) :
    N, J = map(int, f.readline()[:-1].split())
    res = ''
    for n in range(2**(N-2)) :
        b = bin(n)[2:]
        j = '1' + '0'*(N-2-len(b)) + b + '1'
        d = []
        for B in range(2, 11) :
            nb = int(j, B)
            for p in P :
                if nb%p == 0 :
                    # print(j, B, nb, p)
                    d.append(p)
                    break
            if len(d) != B-1 :
                break
        if len(d) == 9 :
            res += '\n' + str(j) + ' ' + ' '.join(map(str, d))
            J -= 1
            if J == 0 : break
    output = 'Case #' + str(case+1) + ': ' + str(res)
    print(output)
    g.write(output + '\n')

f.close()
g.close()
