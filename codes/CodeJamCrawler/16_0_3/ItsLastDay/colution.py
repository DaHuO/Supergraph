coins = []

for i in range(2 ** 31, 2 ** 32 - 1):
    t = bin(i)
    if len(t) != 34 or t[2] != '1' or t[-1] != '1':
        continue

    divs = []
    for base in range(2, 11):
        cur = int(t[2:], base)
        dd = -1

        for div in range(2, min(200, cur)):
            if cur % div == 0:
                dd = div
                break
            
        divs.append(dd)

    if not any(map(lambda x: x == -1, divs)):
        coins.append((t[2:], divs))

    if len(coins) > 500:
        break

f = open('sol.txt', 'w')
for i in range(500):
    print(coins[i][0], ' '.join(map(str, coins[i][1])), file=f)

