from _functools import reduce


def generate(coins):
    if len(coins) == 0:
        return ['0', '1']
    result = []
    for coin in coins:
        result.append(coin + '1')
        result.append(coin + '0')
    return result

def getDivisor(n):
    d = set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))
    d.discard(1)
    d.discard(n)
    return d

def solve(N, J):
    n = N - 2
    coins = []
    for _ in range(n):
        coins = generate(coins)

    result = []
    for coin in coins:
        coin = '1' + coin + '1'
        divisors = []
        for base in range(2, 11):
            i = int(coin, base)
            d = getDivisor(i)
            if len(d) == 0:
                break
            else:
                divisors.append(d.pop())
        if len(divisors) == 9:
            result.append((coin, divisors))
            if len(result) == J:
                break

    s = ""
    for r in result:
        s += r[0] + " " + " ".join([str(x) for x in r[1]]) + "\n"
    return s

file_name = 'input_small'

data = []

with open(file_name, 'r') as f:
    T = int(f.readline())
    for i in range(T):
        N, J = [int(x) for x in f.readline().split()]
        data.append((N, J));

output = ""
for i, datum in enumerate(data):
    output += "Case #" + str(i + 1) + ":\n" + solve(*datum) + "\n"

print(output)
with open('output', 'w') as f:
    f.write(output)
