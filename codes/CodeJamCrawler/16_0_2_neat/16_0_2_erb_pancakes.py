


def flips_str(s):
    l = list(map(lambda x: True if x == "+" else False, s))
    return flips(l)

def flips(l):
    flips = 0
    l = l.copy()
    l.reverse()
    for i in range(len(l)):
        if l[i] == False:
            flips += 1
            for j in range(i, len(l)):
                l[j] = not l[j]
    return flips

assert flips_str("-") == 1
assert flips_str("-+") == 1
assert flips_str("+-") == 2
assert flips_str("+++") == 0
assert flips_str("--+-") == 3

n = int(input())
inputs = [input() for i in range(n)]
results = list(map(lambda s: flips_str(s), inputs))
for i in range(n):
    print("Case #{}: {}".format(i+1, results[i]))






