print("Case #1:")

sieve = [True] * (2 ** 16 + 1)
sieve[0] = False
sieve[1] = False

for i in range(2, len(sieve)):
    if not sieve[i]: continue
    sieve[2*i:len(sieve):i] = [False] * ((len(sieve)-1) // i - 1)

primes = [i for i, v in enumerate(sieve) if v]

start = 2 ** 31 + 1
end = 2 ** 32 - 1

coins = []
for n in range(start, end+1, 2):
    s = bin(n)[2:]
    divisors = []
    for b in range(2, 10+1):
        n = int(s, b)
        res = next((p for p in primes if n % p == 0), None)
        if res:
            divisors.append(res)
        else:
            break
    if len(divisors) == 9:
        coins.append((s, divisors))
    if len(coins) == 500:
        break
        
for s, divisors in coins:
    print(s, ' '.join(map(str, divisors)))