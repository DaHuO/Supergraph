fin = open("C-small-attempt0.in", "r")
fout = open("C-small-attempt0.out", "w")
T, N, J = list(map(lambda x: int(x), fin.read().split()))
n = int('1' * N)
it = 1

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
        if d > 10**6:
            d = n
            break
    return d * d > n, d

fout.write("Case #1:\n")

while J > 0:
    t = bin(int('0' * (N - 1), 2) + it)
    t = t[t.find('b') + 1:]
    tmp = '1' + '0' * (N - 1 - len(t)) + str(int(t, 10))
    result = tmp
    it += 2
    print(J)
    f = 0
    for i in range(2, 11):
        b, d = IsPrime(int(tmp, i))
        if not b:
            result += " " + str(d)
        else:
            f = 1
    if f == 1:
        continue
    fout.write(result + "\n")
    J -= 1

