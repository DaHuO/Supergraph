bs = []
size = 0
primes = []

def isPrime(n):
    global bs
    global size
    global primes
    if n <= size:
        return bs[n]
    total = len(primes)
    for i in range(0, total):
        if n % primes[i] == 0:
            return False
    return True

def sieve(up):
    global bs
    global size
    global primes

    size = up + 1
    bs = [True] * (size + 1)
    bs[0] = False
    bs[1] = False
    for i in range(2, size + 1):
        if bs[i]:
            for j in range(i * i, size + 1, i):
                bs[j] = False
            primes.append(i)

encontrados = 0
def valid(s, MAX):
    global encontrados
    if encontrados != MAX:
        v = []
        for b in range(2, 11):
            num = 0
            base = 1
            for c in reversed(s):
                num = num + (int(c) * base)
                base = base * b
            v.append(num)
            if isPrime(num):
                return False
        for i in range(0, len(v)):
            if v[i] % 2 == 0:
                v[i] = 2
            else:
                for j in range(3, v[i], 2):
                    if v[i] % j == 0:
                        v[i] = j
                        break
        encontrados = encontrados + 1
        print(s, end="")
        for i in range(0, len(v)):
            print(" " + str(v[i]), end="")
        print("")
    return True

def gerar(s, n, MAX):
    if len(s) == n - 1:
        s = s + "1"
        valid(s, MAX)
    else:
        gerar(s + "0", n, MAX)
        gerar(s + "1", n, MAX)

sieve(10000000)
caso = 1
t = int(input())
for T in range(1, t + 1):
    encontrados = 0
    n, j = input().split()
    n = int(n)
    j = int(j)

    print("Case #" + str(T) + ":")
    gerar("1", n, j)
