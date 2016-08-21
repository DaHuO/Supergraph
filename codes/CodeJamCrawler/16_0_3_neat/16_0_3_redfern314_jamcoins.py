cache = {}


def check(coin):
    divisors = [0 for i in range(2, 11)]
    for base in range(2, 11):
        num = int(coin, base)
        if num in cache:
            res = cache[num]
            if not res:
                return False
            divisors[base-2] = res
            continue

        for i in range(2, 100000):
            if num % i == 0:
                # print base, num, coin
                divisors[base-2] = i
                cache[num] = i
                break
        if not divisors[base-2]:
            return False
    return divisors

cases = int(raw_input().strip())
out = open('output.txt', 'w')

for case in range(cases):
    (size, num_coins) = [int(x) for x in raw_input().strip().split()]
    max_inside = int('1'*(size-2), 2)
    coins = []
    for i in range(0, 100000):
        string = '1'+bin(i)[2:].zfill(size-2)+'1'
        divisors = check(string)
        if divisors:
            coins.append((string, divisors))
            print string, divisors
            if len(coins) == num_coins:
                break
    print coins
    s = "Case #"+str(case+1)+":\n"
    for coin in coins:
        s += "%s %s\n" % (coin[0], ' '.join([str(x) for x in coin[1]]))
    out.write(s)
    print(s)
