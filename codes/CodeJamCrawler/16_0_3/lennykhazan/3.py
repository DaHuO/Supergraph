import math



T = int(input())

primes = {1: 1}
def prime(n):
    if n in primes:
        return primes[n]

    if n%2 == 0:
        return 2

    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            primes[n] = i
            return i

    primes[n] = 0
    return 0

def solve(N, J):
    coins = []
    curr = (1 << N - 1) - 1
    while len(coins) < J:
        curr += 2
        divisors = []
        for base in range(2, 11):
            num = 0
            exp = 0
            for char in reversed(bin(curr)[2:]):
                num += base**exp * int(char)
                exp += 1
            divisor = prime(num)
            if divisor == 0:
                break
            else:
                divisors.append(str(divisor))
        if len(divisors) == 9:
            coins.append((curr, divisors))
    return coins

for t in range(T):
    case = [int(x) for x in input().split(' ')]
    print('Case #' + str(t+1) + ':')
    for coin, divisors in solve(case[0], case [1]):
        print(bin(coin)[2:] + ' ' + ' '.join(divisors))
