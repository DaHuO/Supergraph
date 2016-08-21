N_SMALL = 16
J_SMALL = 50
N_BIG = 32
J_BIG = 500

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

def is_jamcoin(a):
    divisors = []
    for i in range(2, 11):
        base_x = long(str(a), i)
        d = is_prime(base_x)
        if d == 0:
            return False
        divisors.append(d)

    return divisors

primes = []

def is_prime(a):
    sr = a **.5
    for i in gen_primes():
        if a % i == 0:
            return i
        if i > sr:
            return 0

def next_coin(a):
    nxt = bin(long(a,2)-2)[2:]
    return nxt

    return a

def get_jamcoins(n, j):
    jamcoins = []
    # coin  = "1" + "1" * (n-2) + "1"
    coin = "10" * (n/2)
    while len(jamcoins) < j:
        divisors = is_jamcoin(coin)
        if divisors != False:
            jamcoins.append((coin, divisors))
            print coin
        coin = next_coin(coin)
    return jamcoins




# print is_jamcoin(1001)
# print next_coin("1000011")
# jamcoins = get_jamcoins(6,3)
jamcoins = get_jamcoins(N_SMALL, J_SMALL)
# jamcoins = get_jamcoins(N_BIG, J_BIG)

with open("output_SMALL_2.txt", "w+") as o:
    o.write("Case #1:\n")
    for jamcoin in jamcoins:
        o.write(jamcoin[0])
        divs = jamcoin[1]
        for div in divs:
            o.write(" ")
            o.write(str(div))
        o.write("\n")
