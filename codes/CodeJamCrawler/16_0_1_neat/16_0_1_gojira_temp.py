def digits(n):
    ret = set()
    while n > 0:
        ret.add(n % 10)
        n /= 10
    return ret


def compute(n):
    if n == 0:
        return "INSOMNIA"
    seen = set(digits(n))
    mul = 1
    while len(seen) < 10:
        mul += 1
        seen.update(digits(n * mul))
    return mul * n

t = int(raw_input())
for i in range(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, compute(n))
