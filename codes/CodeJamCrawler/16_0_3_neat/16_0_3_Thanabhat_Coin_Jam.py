PP = 1000000
isPrime = [True] * 1000000
isPrime[0] = False
isPrime[1] = False
prime = []
for i in range(PP):
    if isPrime[i]:
        for j in range(i * 2, PP, i):
            isPrime[j] = False
for i in range(PP):
    if isPrime[i]:
        prime.append(i)
lenPrime = len(prime)

m = 32769
N = 16
J = 50

m = 2147483649
N = 32
J = 500


def base10toBin(n):
    tmp = n
    sol = [0] * N
    for i in range(N):
        sol[i] = tmp % 2
        tmp = int(tmp / 2)
    return sol


def binToBaseN(n, b):
    sol = 0
    mul = 1
    for i in range(N):
        sol += mul * n[i]
        mul *= b
    return sol


print("Case #1:")

cnt = 0
while (cnt < J):
    m2 = base10toBin(m)
    m += 2
    sol = []
    for i in range(2, 11):
        mn = binToBaseN(m2, i)
        divider = -1
        for j in range(lenPrime):
            if prime[j] * prime[j] >= mn:
                break
            if mn % prime[j] == 0:
                divider = prime[j]
                break
        if divider != -1:
            sol.append(divider)
        else:
            break
    if len(sol) != 9:
        continue
    for i in reversed(range(0, N)):
        print(m2[i], end='')
    for i in range(9):
        print(' ' + str(sol[i]), end='')
    print('')
    cnt += 1
