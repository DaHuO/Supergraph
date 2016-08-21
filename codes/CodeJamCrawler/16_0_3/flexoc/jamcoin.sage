import random
def randcoin(n):
    s = "1"
    for i in range(n-2):
        s += random.choice(["1", "0"])
    return s + "1"

T = input()
assert(T == 1)
N, J = [int(_) for _ in raw_input().split()]
coins = {}
while len(coins) < J:
    x = randcoin(N)
    if x in coins:
        continue
    pr = []
    for i in xrange(2, 11):
        y = ZZ(x, base=i)
        if y.is_prime():
            break
        pr.append(y.factor()[0][0])
    else:
        coins[x] = pr


print("Case #1:")
for c, pr in coins.iteritems():
    print("%s %s" % (c, " ".join(str(x) for x in pr)))
